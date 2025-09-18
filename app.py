import os
from uuid import uuid4
import streamlit as st
from dotenv import load_dotenv

from scraper import scrape_blog
from summarizer import summarize_text
from tts import generate_speech

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

# Default voice (only one option now)
voice_id = "pNInz6obpgDQGcFmaJgB"  # Arjun (Male, default)

# LLM Provider selection (only OpenAI & Ollama)
llm_provider = st.selectbox(
    "🤖 Choose LLM Provider",
    ["OpenAI", "Ollama (Mistral)"]
)

generate_button = st.button("🎙️ Generate Podcast")

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

        with st.spinner(f"Summarizing content with {llm_provider}..."):
            summary = summarize_text(blog_text, provider=llm_provider)
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
