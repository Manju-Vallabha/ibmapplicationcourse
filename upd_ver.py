import streamlit as st
import os
import google.generativeai as genai
from streamlit_lottie import st_lottie
import json
from dotenv import load_dotenv
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Lottie animation from a file
def load_lottiefile(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

# Streamlit app setup
st.set_page_config(page_title='BlogMaster', page_icon='🧊', layout='wide', initial_sidebar_state='auto')
ai = load_lottiefile("ai.json")

# Title
st.title('🤖 BlogMaster: AI-Powered Blog Generator')

# Subheader
st.header('✨ Generate captivating blog content in seconds with AI magic 🚀')
st_lottie(ai, speed=1, reverse=False, quality="low", loop=True, height=250)

# Sidebar for user input
with st.sidebar:
    st.title('📝 Enter your blog details')

    # Blog title
    blog_title = st.text_input('Title')

    # Blog keywords
    blog_keywords = st.text_area('Keywords')

    # Number of words
    num_words = st.slider('Number of Words', 250, 1000, 250)

    # Generate button
    submit_button = st.button('Generate Blog')

# Generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

if not blog_title or not blog_keywords:
    st.warning("Please provide a title and keywords for the blog!")

# Handle blog generation
if submit_button:
    if not blog_title or not blog_keywords:
        st.error("Please provide a title and keywords for the blog!")
    else:
        # Display loading spinner
        with st.spinner("Generating your blog..."):
            # Create the model
            model = genai.GenerativeModel(
                model_name="gemini-2.0-flash-exp",
                generation_config=generation_config,
            )

            chat_session = model.start_chat(
                history=[{
                    "role": "user",
                    "parts": [
                        f"Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords \"{blog_keywords}\". Make sure to incorporate these keywords in the blog post. The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout.",
                    ],
                }]
            )
            
            prompt = f"Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords \"{blog_keywords}\". Make sure to incorporate these keywords in the blog post. The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout."
            response = chat_session.send_message(content=prompt)

            # Full blog content display after generation
            st.info("Blog generated succcessfully! 🚀")
            st.success(response.text)

            # Provide download option
            st.download_button(
                label="Download as Text",
                data=response.text,
                file_name=f"{blog_title}.txt",
                mime="text/plain",
            )
