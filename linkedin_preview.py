import streamlit as st
from datetime import datetime
import random

class LinkedInPreview:
    def __init__(self):
        self.sample_names = [
            "Sarah Johnson", "Michael Chen", "Emily Rodriguez", "David Kim", 
            "Lisa Thompson", "Alex Martinez", "Jessica Brown", "Ryan Wilson",
            "Amanda Davis", "Chris Taylor", "Maria Garcia", "James Anderson",
            "Samarth Nehe", "Priya Sharma", "Raj Patel", "Anita Singh"
        ]
        self.sample_titles = [
            "SDE II @Uber | Helping engineers land their dream jobs | Typescript, React",
            "Software Engineer at Google | Building scalable systems | Python, Go",
            "Product Manager at Microsoft | Driving innovation in cloud computing",
            "Data Scientist at Amazon | ML/AI enthusiast | Python, TensorFlow",
            "UX Designer at Meta | Creating user-centered experiences | Figma, Sketch",
            "Business Analyst at Goldman Sachs | Finance & Strategy | Excel, SQL",
            "Sales Director at Salesforce | Driving revenue growth | CRM, B2B",
            "HR Specialist at LinkedIn | People & Culture | Talent Acquisition",
            "Operations Manager at Tesla | Supply Chain & Manufacturing",
            "Consultant at McKinsey | Strategy & Operations | Problem Solving",
            "Marketing Manager at Netflix | Content & Growth | Digital Marketing",
            "DevOps Engineer at Spotify | Infrastructure & Automation | AWS, Docker"
        ]
        self.sample_companies = [
            "Uber", "Google", "Microsoft", "Amazon", "Meta", "Goldman Sachs",
            "Salesforce", "LinkedIn", "Tesla", "McKinsey", "Netflix", "Spotify"
        ]
    
    def generate_sample_user(self):
        """Generate a random sample user for preview"""
        return {
            "name": random.choice(self.sample_names),
            "title": random.choice(self.sample_titles),
            "company": random.choice(self.sample_companies),
            "time": self._get_random_time(),
            "avatar_url": self._get_random_avatar()
        }
    
    def _get_random_avatar(self):
        """Generate a random avatar URL"""
        # Using a service that provides random profile pictures
        avatar_id = random.randint(1, 100)
        return f"https://i.pravatar.cc/150?img={avatar_id}"
    
    def _get_random_time(self):
        """Generate random time for post"""
        times = [
            "2h", "4h", "6h", "1d", "2d", "3d", "1w", "2w"
        ]
        return random.choice(times)
    
    def render_linkedin_preview(self, post_content, hashtags=None, user=None):
        """
        Render a LinkedIn-style preview of the post
        """
        if user is None:
            user = self.generate_sample_user()
        
        
        likes = random.randint(5, 150)
        comments = random.randint(0, 25)
        shares = random.randint(0, 15)
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                .linkedin-preview {{
                    border: 1px solid #e0e0e0;
                    border-radius: 8px;
                    background-color: #ffffff;
                    padding: 16px;
                    margin: 10px 0;
                    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                    max-width: 100%;
                    min-height: 200px;
                    overflow: hidden;
                }}
                .linkedin-header {{
                    display: flex;
                    align-items: flex-start;
                    margin-bottom: 12px;
                    position: relative;
                }}
                .linkedin-avatar {{
                    width: 48px;
                    height: 48px;
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin-right: 12px;
                    flex-shrink: 0;
                    overflow: hidden;
                }}
                .linkedin-avatar img {{
                    width: 100%;
                    height: 100%;
                    object-fit: cover;
                    border-radius: 50%;
                }}
                .linkedin-avatar-fallback {{
                    width: 48px;
                    height: 48px;
                    border-radius: 50%;
                    background: linear-gradient(45deg, #0077b5, #005885);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: white;
                    font-weight: bold;
                    font-size: 18px;
                }}
                .linkedin-user-info {{
                    flex: 1;
                    min-width: 0;
                }}
                .linkedin-user-info h3 {{
                    margin: 0 0 2px 0;
                    font-size: 14px;
                    font-weight: 600;
                    color: #000000;
                    line-height: 1.2;
                }}
                .linkedin-user-info .verified {{
                    display: inline-block;
                    width: 16px;
                    height: 16px;
                    margin-left: 4px;
                    position: relative;
                    vertical-align: middle;
                    margin-top: -1px;
                }}
                .linkedin-user-info .verified svg {{
                    width: 16px;
                    height: 16px;
                }}
                .linkedin-user-info p {{
                    margin: 0;
                    font-size: 12px;
                    color: #666666;
                    line-height: 1.3;
                }}
                .linkedin-user-info .connection {{
                    font-size: 12px;
                    color: #666666;
                    margin-left: 4px;
                }}
                .linkedin-time {{
                    font-size: 12px;
                    color: #666666;
                    display: flex;
                    align-items: center;
                    margin-top: 4px;
                }}
                .linkedin-time .globe {{
                    margin-left: 4px;
                    font-size: 10px;
                }}
                .linkedin-content {{
                    font-size: 14px;
                    line-height: 1.4;
                    color: #000000;
                    margin-bottom: 12px;
                    white-space: pre-wrap;
                    word-wrap: break-word;
                }}
                .linkedin-content strong {{
                    font-weight: 600;
                }}
                .linkedin-hashtags {{
                    color: #0077b5;
                    font-size: 14px;
                    margin-top: 8px;
                    margin-bottom: 12px;
                    line-height: 1.4;
                }}
                .linkedin-actions {{
                    display: flex;
                    align-items: center;
                    margin-top: 12px;
                    padding-top: 12px;
                    border-top: 1px solid #e0e0e0;
                    flex-wrap: wrap;
                    gap: 8px;
                }}
                .linkedin-action {{
                    display: flex;
                    align-items: center;
                    color: #666666;
                    font-size: 14px;
                    cursor: pointer;
                    padding: 4px 8px;
                    border-radius: 4px;
                    gap: 6px;
                    flex-shrink: 0;
                }}
                .linkedin-action svg {{
                    flex-shrink: 0;
                    width: 20px;
                    height: 20px;
                }}
                .linkedin-action:hover {{
                    color: #0077b5;
                    background-color: #f3f2ef;
                }}
                .linkedin-engagement {{
                    display: flex;
                    align-items: center;
                    margin-bottom: 8px;
                    padding: 0 4px;
                }}
                .linkedin-engagement .likes {{
                    font-size: 12px;
                    color: #666666;
                }}
                .linkedin-engagement .likes strong {{
                    color: #000000;
                }}
            </style>
        </head>
        <body>
            <div class="linkedin-preview">
                <div class="linkedin-header">
                    <div class="linkedin-avatar">
                        <img src="{user.get('avatar_url', '')}" alt="{user['name']}" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                        <div class="linkedin-avatar-fallback" style="display: none;">{user['name'][0]}</div>
                    </div>
                    <div class="linkedin-user-info">
                        <h3>{user['name']}<span class="verified"><svg viewBox="0 0 24 24" fill="white" stroke="black" stroke-width="1.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4" fill="black"/></svg></span><span class="connection">• 2nd</span></h3>
                        <p>{user['title']}</p>
                        <div class="linkedin-time">{user['time']} • <span class="globe">🌐</span></div>
                    </div>
                </div>
                
                <div class="linkedin-content">{post_content}</div>
                
                {f'<div class="linkedin-hashtags">{" ".join(hashtags) if hashtags else ""}</div>' if hashtags else ''}
                
                <div class="linkedin-engagement">
                    <div class="likes">
                        {f'<strong>{likes}</strong> likes' if likes > 0 else ''}
                        {f' • {comments} comments' if comments > 0 else ''}
                        {f' • {shares} shares' if shares > 0 else ''}
                    </div>
                </div>
                
                <div class="linkedin-actions">
                    <div class="linkedin-action">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M7 13l3 3 7-7"/>
                            <path d="M21 12c0 4.97-4.03 9-9 9s-9-4.03-9-9 4.03-9 9-9 9 4.03 9 9z"/>
                        </svg>
                        Like
                    </div>
                    <div class="linkedin-action">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
                        </svg>
                        Comment
                    </div>
                    <div class="linkedin-action">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"/>
                            <polyline points="16,6 12,2 8,6"/>
                            <line x1="12" y1="2" x2="12" y2="15"/>
                        </svg>
                        Repost
                    </div>
                    <div class="linkedin-action">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <line x1="22" y1="2" x2="11" y2="13"/>
                            <polygon points="22,2 15,22 11,13 2,9 22,2"/>
                        </svg>
                        Send
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
        
        st.components.v1.html(html_content, height=400, scrolling=True)
    
    def render_multiple_previews(self, variations):
        """
        Render multiple LinkedIn previews for variations
        """
        for i, variation in enumerate(variations):
            st.subheader(f"LinkedIn Preview - Variation {variation['variation']}")
            user = self.generate_sample_user()
            self.render_linkedin_preview(
                variation['content'], 
                variation.get('hashtags', []), 
                user
            )
            
            if i < len(variations) - 1:
                st.markdown("---")

if __name__ == "__main__":
    # Test the LinkedIn preview
    preview = LinkedInPreview()
    
    test_post = "Just finished an amazing project! The key to success is consistency and never giving up. What's your biggest challenge this week?"
    test_hashtags = ["#motivation", "#success", "#career", "#growth", "#professional"]
    
    print("LinkedIn Preview Test:")
    preview.render_linkedin_preview(test_post, test_hashtags)
