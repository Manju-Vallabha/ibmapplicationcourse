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

# Handle blog generation
if submit_button:
    if not blog_title or not blog_keywords:
        st.error("Please provide a title and keywords for the blog!")
    else:
        st.info('🤖 Generating blog content... Please wait for a few seconds...')
        
        # Create the model
        model = genai.GenerativeModel(
            model_name="gemini-2.0-flash-exp",
            generation_config=generation_config,
        )

        chat_session = model.start_chat(
        history=[
    {
      "role": "user",
      "parts": [
        "Generate a comprehensive, engaging blog post relevant to the given title \"Effects of Generative Al\" and keywords \"Artificial Creativity, Ethical Implications, Technology Innovation, Machine Learning Applications, Al Impact on Society\". Make sure to incorporate these keywords in the blog post. The blog should be approximately 500 words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, here's a blog post designed to fit your requirements:\n\n**The Generative AI Revolution: Creativity, Ethics, and the Shaping of Our Future**\n\nThe world is buzzing with the potential of Generative AI, and for good reason. These incredible algorithms, powered by complex **machine learning applications**, are no longer confined to crunching numbers; they’re composing music, writing stories, designing architecture, and even creating artwork. This is the rise of **Artificial Creativity**, and it's fundamentally changing how we think about innovation, creation, and the role of technology in our lives.\n\nGenerative AI's power stems from its ability to learn from massive datasets and generate new content that resembles its training data. Think of it as a digital apprentice, capable of not just mimicking but innovating based on what it’s absorbed. This opens doors to groundbreaking **technology innovation** across countless fields. In medicine, AI can design new drugs and personalized treatments. In engineering, it’s accelerating the design process for everything from cars to bridges. In the arts, it’s enabling artists to explore previously unimaginable creative avenues.\n\nBut with this immense power comes responsibility. The **ethical implications** of generative AI are profound and demand careful consideration. Who owns the copyright to AI-generated art? How do we ensure AI tools are used for good, not for malicious purposes like creating deepfakes or spreading misinformation? What are the economic consequences of automated content creation on human artists and creators? These are not abstract, future concerns; they are very real questions we need to address today.\n\nOne of the biggest societal impacts is the potential displacement of certain jobs. As AI becomes more adept at writing, coding, and even creating visual content, questions arise about the future of human employment in these areas. We must be proactive in preparing for these changes, focusing on reskilling and upskilling the workforce to thrive in an AI-driven economy. However, the narrative shouldn't solely focus on displacement. Generative AI also opens up new avenues for human collaboration. Imagine artists using AI as a powerful tool to enhance their creative process, or developers utilizing AI-powered assistants to accelerate their workflows. The future likely lies in a partnership between human ingenuity and AI capabilities.\n\nMoreover, the **Al Impact on Society** will extend beyond just job markets. Consider how AI-generated content influences public discourse, how it impacts learning and education, or even how it shapes our perception of reality. The pervasive nature of these technologies means we must foster critical thinking and digital literacy to navigate this evolving landscape. We need to understand how AI operates, its limitations, and its biases, so we can use it responsibly and ethically.\n\nThe generative AI revolution is undeniably underway. It’s a powerful force for both progress and potential peril. By embracing innovation while acknowledging its ethical complexities, we can ensure that this technology benefits all of humanity. The journey is just beginning, and it’s our collective responsibility to shape it in a way that reflects our highest values and aspirations. It's not just about understanding the tech; it's about understanding the human impact and navigating a future where AI becomes an integral part of our lives. The key is to be proactive, thoughtful, and open to a future shaped by both human creativity and the boundless potential of Artificial Intelligence.\n",
      ],
    },
  ]
)
        prompt = f"Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords \"{blog_keywords}\". Make sure to incorporate these keywords in the blog post. The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout."
        response = chat_session.send_message(content=prompt)

        # Display response
        st.write(response.text)
