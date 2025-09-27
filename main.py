import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post, generate_multiple_posts
from linkedin_preview import LinkedInPreview

length_options=["Short","Medium","Long"]
language_options=["English","Hinglish"]

def main():
    st.title("LinkedIn Post Generator")
    
    if 'generated_posts' not in st.session_state:
        st.session_state.generated_posts = None
    if 'show_variations' not in st.session_state:
        st.session_state.show_variations = False
    
    col1,col2,col3 = st.columns(3)
    fs = FewShotPosts()
    with col1:
        selected_tag = st.selectbox("Title",options=fs.get_tags())

    with col2:
        selected_length = st.selectbox("Length",options=length_options)

    with col3:
        selected_language = st.selectbox("Language",options=language_options)

    col4, col5, col6 = st.columns([1, 1, 1])
    with col4:
        generate_variations = st.checkbox("Generate multiple variations", value=False)
        if generate_variations:
            num_variations = st.number_input("Variations", min_value=2, max_value=5, value=3, 
                                           help="2-5 variations")
    
    with col5:
        include_hashtags = st.checkbox("Include hashtags", value=True)
    
    with col6:
        show_preview = st.checkbox("Show LinkedIn preview", value=True)
    
    if st.button("Generate"):
        if generate_variations:
            with st.spinner("Generating multiple post variations..."):
                variations = generate_multiple_posts(selected_length, selected_language, selected_tag, num_variations=num_variations, include_hashtags=include_hashtags)
            
            st.session_state.generated_posts = {
                'type': 'variations',
                'data': variations,
                'include_hashtags': include_hashtags,
                'show_preview': show_preview
            }
            st.session_state.show_variations = True
        else:
            post_data = generate_post(selected_length, selected_language, selected_tag, include_hashtags=include_hashtags)
            
            st.session_state.generated_posts = {
                'type': 'single',
                'data': post_data,
                'include_hashtags': include_hashtags,
                'show_preview': show_preview
            }
            st.session_state.show_variations = False
    
    if st.session_state.generated_posts is not None:
        if st.session_state.generated_posts['type'] == 'variations':
            st.subheader("Generated Post Variations:")
            
            preview = LinkedInPreview()
            variations = st.session_state.generated_posts['data']
            include_hashtags = st.session_state.generated_posts['include_hashtags']
            show_preview = st.session_state.generated_posts['show_preview']
            
            for i, variation in enumerate(variations):
                with st.expander(f"Variation {variation['variation']}", expanded=(i==0)):
                    st.write(variation['content'])
                    
                    if include_hashtags and variation['hashtags']:
                        st.write("**Suggested Hashtags:**")
                        hashtag_text = " ".join(variation['hashtags'])
                        st.write(hashtag_text)
                    
                    if show_preview:
                        if st.button(f"See LinkedIn Preview - Variation {variation['variation']}", key=f"preview_{i}"):
                            st.write("**LinkedIn Preview:**")
                            preview.render_linkedin_preview(
                                variation['content'], 
                                variation.get('hashtags', []) if include_hashtags else None
                            )
        else:
            st.subheader("Generated Post:")
            post_data = st.session_state.generated_posts['data']
            include_hashtags = st.session_state.generated_posts['include_hashtags']
            show_preview = st.session_state.generated_posts['show_preview']
            
            st.write(post_data['content'])
            
            if include_hashtags and post_data['hashtags']:
                st.write("**Suggested Hashtags:**")
                hashtag_text = " ".join(post_data['hashtags'])
                st.write(hashtag_text)
            
            if show_preview:
                if st.button("See LinkedIn Preview", key="preview_single"):
                    st.write("**LinkedIn Preview:**")
                    preview = LinkedInPreview()
                    preview.render_linkedin_preview(
                        post_data['content'], 
                        post_data.get('hashtags', []) if include_hashtags else None
                    )
if __name__ == "__main__":
    main()