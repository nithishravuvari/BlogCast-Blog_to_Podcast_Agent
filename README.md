# 📰 → 🎧 BlogCast : Blog to Podcast Agent

Transform any blog post into an engaging podcast in minutes!


## ✨ Features

✅ **Scrape blog content** from any public URL  
✅ **Summarize text** using LLMs via Ollama (e.g., Mistral, Llama)  
✅ **Convert summaries to speech** using ElevenLabs realistic voices  
✅ **Download podcasts and transcripts** for offline use  
✅ **Choose male or female voices** for narration  


## 🚀 Quick Start

Follow these steps to set up and run the app:


### 1️⃣ Clone the repository

```bash
git clone https://github.com/nithishravuvari/BlogCast-Blog_to_Podcast_Agent.git

cd BlogCast-Blog_to_Podcast_Agent
```


### 2️⃣ Install dependencies

Make sure you have Python 3.8+ installed.

```bash
pip install -r requirements.txt
```

### 3️⃣ Set up environment variables

Create a .env file in the project directory and add your ElevenLabs API key:

```bash
# .env
ELEVEN_LABS_API_KEY=your_elevenlabs_api_key_here
```

### 4️⃣ Start the Ollama server

If you haven’t already, install Ollama and start your model:
```bash
ollama serve
```

Then pull and run the desired model (e.g., mistral):
```bash
ollama pull mistral
```

### 5️⃣ Launch the Streamlit app
```bash
streamlit run blog_to_podcast_agent.py
```

## 💡 How It Works

1. **Paste the blog URL** into the input field.
2. **Choose a voice** (male or female) for narration.
3. Click **🎙️ Generate Podcast**.
4. BlogCast will automatically:
   - Scrape and extract the blog content.
   - Summarize the text using an LLM (Ollama).
   - Generate high-quality audio narration with ElevenLabs.
5. **Listen** to your podcast instantly or **download** it for offline use.



## 📸 Snapshots
![image](https://github.com/user-attachments/assets/21f86502-67dc-4a5d-a951-1453c3473063)
![image](https://github.com/user-attachments/assets/1f0ea354-b09f-4e93-9881-f9de64549fd9)
![image](https://github.com/user-attachments/assets/bb6c6232-7e29-40ad-8646-9ec2719f28a3)


