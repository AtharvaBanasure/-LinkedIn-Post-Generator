import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post, generate_multiple_posts

length_options=["Short","Medium","Long"]
language_options=["English","Hinglish"]

def main():
    st.title("LinkedIn Post Generator")
    col1,col2,col3 = st.columns(3)
    fs = FewShotPosts()
    with col1:
        selected_tag = st.selectbox("Title",options=fs.get_tags())

    with col2:
        selected_length = st.selectbox("Length",options=length_options)

    with col3:
        selected_language = st.selectbox("Language",options=language_options)

    col4, col5 = st.columns([1, 1])
    with col4:
        generate_variations = st.checkbox("Generate multiple variations", value=False)
        if generate_variations:
            num_variations = st.number_input("Variations", min_value=2, max_value=5, value=3, 
                                           help="2-5 variations")
    
    with col5:
        include_hashtags = st.checkbox("Include hashtags", value=True)
    
    if st.button("Generate"):
        if generate_variations:
            # Generate multiple variations
            with st.spinner("Generating multiple post variations..."):
                variations = generate_multiple_posts(selected_length, selected_language, selected_tag, num_variations=num_variations, include_hashtags=include_hashtags)
            
            st.subheader("Generated Post Variations:")
            
            for i, variation in enumerate(variations):
                with st.expander(f"Variation {variation['variation']}", expanded=(i==0)):
                    st.write(variation['content'])
                    
                    if include_hashtags and variation['hashtags']:
                        st.write("**Suggested Hashtags:**")
                        hashtag_text = " ".join(variation['hashtags'])
                        st.write(hashtag_text)
        else:
            post_data = generate_post(selected_length, selected_language, selected_tag, include_hashtags=include_hashtags)
            st.subheader("Generated Post:")
            st.write(post_data['content'])
            
            if include_hashtags and post_data['hashtags']:
                st.write("**Suggested Hashtags:**")
                hashtag_text = " ".join(post_data['hashtags'])
                st.write(hashtag_text)
if __name__ == "__main__":
    main()