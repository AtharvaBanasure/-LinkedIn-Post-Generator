from few_shot import FewShotPosts
from llm_helper import llm
from hashtag_generator import HashtagGenerator

few_shot = FewShotPosts()

def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"


def get_prompt(length,language,tag):
    length_str = get_length_str(length)
    prompt = f'''
            Generate a LinkedIn Post using the below information. No preamble.

            1) Topic: {tag}
            2) Length: {length_str}
            3) Language: {language}
            If Language is Hinglish it means it is mix of Hindi and English.
            The script for the generated post should always be English.
        '''

    examples = few_shot.get_filterd_posts(length, language, tag)

    if len(examples) > 0:
        prompt += "4) Use the writing style as per the following examples."
        for i, post in enumerate(examples):
            post_text = post["content"]
            prompt += f"\n\nExample {i+1}\n\n {post_text}"

            if i == 2:
                break

    return prompt



def generate_post(length,language,tag,include_hashtags=True):
    prompt = get_prompt(length,language,tag)
    response = llm.invoke(prompt)
    post_content = response.content
    
    # Generate hashtags if requested
    hashtags = []
    if include_hashtags:
        hashtag_generator = HashtagGenerator()
        hashtags = hashtag_generator.generate_hashtags(post_content, tag, num_hashtags=5)
    
    return {
        "content": post_content,
        "hashtags": hashtags
    }

def generate_multiple_posts(length,language,tag,num_variations=3,include_hashtags=True):
    """
    Generate multiple variations of the same post
    """
    variations = []
    base_prompt = get_prompt(length,language,tag)
    hashtag_generator = HashtagGenerator()
    
    for i in range(num_variations):
        # Add variation instruction to make each post different
        variation_prompt = base_prompt + f"\n\n5) This is variation {i+1} of {num_variations}. Make this post unique and different from other variations while keeping the same topic and length."
        response = llm.invoke(variation_prompt)
        
        post_content = response.content
        
        # Generate hashtags if requested
        hashtags = []
        if include_hashtags:
            hashtags = hashtag_generator.generate_hashtags(post_content, tag, num_hashtags=5)
        
        variations.append({
            "variation": i+1,
            "content": post_content,
            "hashtags": hashtags
        })
    
    return variations


if __name__ == "__main__":
    post =  generate_post("Short","English","Job Search")
    print(post)