from llm_helper import llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
import json

class HashtagGenerator:
    def __init__(self):
        self.json_parser = JsonOutputParser()
    
    def generate_hashtags(self, post_content, topic, num_hashtags=5):
        """
        Generate relevant hashtags for a LinkedIn post
        """
        try:
            prompt_template = """
            Generate relevant hashtags for this LinkedIn post. Follow these guidelines:
            
            1. Generate exactly {num_hashtags} hashtags
            2. Make hashtags relevant to the post content and topic
            3. Mix popular hashtags with niche ones
            4. Include the main topic as a hashtag
            5. Use proper LinkedIn hashtag format (no spaces, use camelCase)
            6. Return as JSON array: ["#hashtag1", "#hashtag2", ...]
            
            Post Content: {post_content}
            Topic: {topic}
            
            Generate hashtags:
            """
            
            prompt = PromptTemplate.from_template(prompt_template)
            chain = prompt | llm
            
            response = chain.invoke({
                "post_content": post_content,
                "topic": topic,
                "num_hashtags": num_hashtags
            })
            
            hashtags = self.json_parser.parse(response.content)
            
            formatted_hashtags = []
            for hashtag in hashtags:
                if not hashtag.startswith('#'):
                    hashtag = '#' + hashtag
                formatted_hashtags.append(hashtag)
            
            return formatted_hashtags[:num_hashtags]
            
        except (OutputParserException, json.JSONDecodeError, Exception) as e:
            # Fallback to basic hashtags if LLM parsing fails
            return self._generate_fallback_hashtags(topic, num_hashtags)
    
    def _generate_fallback_hashtags(self, topic, num_hashtags):
        """
        Generate basic hashtags as fallback
        """
        topic_hashtags = {
            "Job Search": ["#JobSearch", "#Career", "#Hiring", "#Opportunity", "#Professional"],
            "Motivation": ["#Motivation", "#Success", "#Inspiration", "#Mindset", "#Growth"],
            "Productivity": ["#Productivity", "#Efficiency", "#TimeManagement", "#Focus", "#WorkSmart"],
            "Networking": ["#Networking", "#Connections", "#Professional", "#Career", "#Business"],
            "Learning": ["#Learning", "#Education", "#Skills", "#Development", "#Growth"],
            "Leadership": ["#Leadership", "#Management", "#Team", "#Success", "#Professional"],
            "Technology": ["#Technology", "#Innovation", "#Digital", "#Tech", "#Future"],
            "Entrepreneurship": ["#Entrepreneurship", "#Startup", "#Business", "#Innovation", "#Success"],
            "Personal Development": ["#PersonalDevelopment", "#Growth", "#Mindset", "#Success", "#Learning"],
            "Career Advice": ["#CareerAdvice", "#Professional", "#Success", "#Growth", "#Career"]
        }
        
        # Get topic-specific hashtags or use generic ones
        hashtags = topic_hashtags.get(topic, ["#Professional", "#Career", "#Success", "#Growth", "#Learning"])
        
        return hashtags[:num_hashtags]
    
    def suggest_hashtag_categories(self, post_content):
        """
        Suggest different categories of hashtags for a post
        """
        try:
            prompt_template = """
            Analyze this LinkedIn post and suggest hashtags in different categories:
            
            Post: {post_content}
            
            Return JSON with these categories:
            {{
                "industry": ["#IndustryHashtag1", "#IndustryHashtag2"],
                "skill": ["#SkillHashtag1", "#SkillHashtag2"], 
                "trending": ["#TrendingHashtag1", "#TrendingHashtag2"],
                "niche": ["#NicheHashtag1", "#NicheHashtag2"]
            }}
            
            Generate 2 hashtags per category:
            """
            
            prompt = PromptTemplate.from_template(prompt_template)
            chain = prompt | llm
            
            response = chain.invoke({"post_content": post_content})
            
            return self.json_parser.parse(response.content)
            
        except Exception as e:
            # Fallback to basic categories
            return {
                "industry": ["#Professional", "#Business"],
                "skill": ["#Skills", "#Development"],
                "trending": ["#Trending", "#Popular"],
                "niche": ["#Niche", "#Specific"]
            }

if __name__ == "__main__":
    # Test the hashtag generator
    generator = HashtagGenerator()
    
    test_post = "Just finished an amazing project! The key to success is consistency and never giving up. What's your biggest challenge this week?"
    test_topic = "Motivation"
    
    print("Generated Hashtags:")
    hashtags = generator.generate_hashtags(test_post, test_topic, 5)
    print(hashtags)
    
    print("\nHashtag Categories:")
    categories = generator.suggest_hashtag_categories(test_post)
    for category, tags in categories.items():
        print(f"{category}: {tags}")
