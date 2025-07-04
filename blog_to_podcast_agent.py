import os
from uuid import uuid4
import requests
from bs4 import BeautifulSoup
import streamlit as st
from dotenv import load_dotenv

from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Streamlit page config
st.set_page_config(page_title="📰 → 🎧 BlogCast", page_icon="🎙️")
st.title("📰 → 🎧 BlogCast")
st.subheader("Transform any blog into an engaging podcast in minutes!")

# Load ElevenLabs API Key
elevenlabs_api_key = os.getenv("ELEVEN_LABS_API_KEY")

if not elevenlabs_api_key:
    st.error("🚨 ELEVEN_LABS_API_KEY not found in environment. Please set it in your .env file.")
    st.stop()

# Input: Blog URL
url = st.text_input("Enter the Blog URL:")

# Voice selection (2 only: 1 male, 1 female)
voice_options = {
    "Arjun (Male)": "pNInz6obpgDQGcFmaJgB",      # Adam
    "Priya (Female)": "21m00Tcm4TlvDq8ikWAM"      # Rachel
}
voice_label = st.selectbox("🎤 Choose a Voice", list(voice_options.keys()))
voice_id = voice_options[voice_label]

generate_button = st.button("🎙️ Generate Podcast")

def scrape_blog(url):
    """Fetch and extract text from a webpage."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        text = "\n".join(p.get_text() for p in paragraphs)
        return text.strip()
    except requests.RequestException as e:
        st.error(f"🌐 Failed to fetch the blog: {e}")
        return None

def summarize_text(text, model_name="mistral"):
    """Summarize text using Ollama."""
    try:
        llm = ChatOllama(model=model_name)
        prompt = ChatPromptTemplate.from_template(
            """
            Summarize the following blog content in a clear, conversational style. Keep it under 2000 characters:

            {blog_text}
            """
        )
        chain = prompt | llm
        return chain.invoke({"blog_text": text}).content
    except Exception as e:
        st.error(f"🤖 Summarization failed: {e}")
        return None

def generate_speech(text, api_key, voice_id):
    """Generate speech audio using ElevenLabs."""
    try:
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
        headers = {
            "xi-api-key": api_key,
            "Content-Type": "application/json"
        }
        payload = {
            "model_id": "eleven_multilingual_v2",
            "text": text,
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75
            }
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            raise Exception(f"ElevenLabs error: {response.text}")
        return response.content
    except Exception as e:
        st.error(f"🎤 Text-to-speech failed: {e}")
        return None

if generate_button:
    if not url.strip():
        st.warning("Please enter a blog URL first.")
    else:
        with st.spinner("Scraping blog content..."):
            blog_text = scrape_blog(url)
            if not blog_text:
                st.stop()
            if len(blog_text) < 50:
                st.error("Could not extract enough text. Please try a different URL.")
                st.stop()
            st.success("✅ Blog content extracted!")

        with st.spinner("Summarizing content..."):
            summary = summarize_text(blog_text)
            if not summary:
                st.stop()
            st.success("✅ Summary ready!")

        st.text_area("📝 Generated Summary", summary, height=200)

        with st.spinner("Generating podcast audio..."):
            audio_data = generate_speech(summary, elevenlabs_api_key, voice_id)
            if not audio_data:
                st.stop()

            save_dir = "audio_generations"
            os.makedirs(save_dir, exist_ok=True)

            # Save audio
            audio_filename = f"{save_dir}/podcast_{uuid4()}.wav"
            with open(audio_filename, "wb") as f:
                f.write(audio_data)

            st.success("✅ Podcast generated successfully!")

            audio_bytes = open(audio_filename, "rb").read()
            st.audio(audio_bytes, format="audio/wav")

            # Download podcast
            st.download_button(
                label="💾 Download Podcast",
                data=audio_bytes,
                file_name="generated_podcast.wav",
                mime="audio/wav"
            )

            # Download transcript
            st.download_button(
                label="💬 Download Transcript",
                data=summary,
                file_name="blogcast_transcript.txt",
                mime="text/plain"
            )
