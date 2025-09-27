from few_shot import FewShotPosts
from llm_helper import llm

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



def generate_post(length,language,tag):
    prompt = get_prompt(length,language,tag)
    response = llm.invoke(prompt)
    return response.content

def generate_multiple_posts(length,language,tag,num_variations=3):
    """
    Generate multiple variations of the same post
    """
    variations = []
    base_prompt = get_prompt(length,language,tag)
    
    for i in range(num_variations):
        # Add variation instruction to make each post different
        variation_prompt = base_prompt + f"\n\n5) This is variation {i+1} of {num_variations}. Make this post unique and different from other variations while keeping the same topic and length."
        response = llm.invoke(variation_prompt)
        variations.append({
            "variation": i+1,
            "content": response.content
        })
    
    return variations


if __name__ == "__main__":
    post =  generate_post("Short","English","Job Search")
    print(post)