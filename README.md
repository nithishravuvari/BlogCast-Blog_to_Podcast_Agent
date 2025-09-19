# 📰 → 🎧 BlogCast

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![LLM's](https://img.shields.io/badge/LLM-663399?style=for-the-badge&logo=openai&logoColor=white)]()
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
[![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.ai/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![ElevenLabs](https://img.shields.io/badge/ElevenLabs-2E6BEB?style=for-the-badge&logo=elevenlabs&logoColor=white)](https://elevenlabs.io/)

Transform any blog into an engaging podcast in minutes!

BlogCast is a Streamlit-based application that converts any blog post into a podcast-style narration. It extracts blog content, summarizes it using your choice of LLM provider (OpenAI or Ollama Mistral), and then generates natural speech using Text-to-Speech.

---

## 📑 Table of Contents

* [Features](#1-features)
* [Project Structure](#2-project-structure)
* [Setup & Installation](#3-setup--installation)
* [Usage](#4-usage)
* [Screenshots](#5-screenshots)

---

## 1. Features

* **🌐 Extract blog content from any URL**: Simply paste a blog link, and the app will do the rest.
* **🤖 Choose your LLM provider**:
    * **OpenAI**: For fast and accurate summaries.
    * **Ollama Mistral**: For local, privacy-friendly processing.
* **🎤 Customizable podcast voices via ElevenLabs**: Select from a variety of voices to give your podcast a unique feel.
* **⚡ Fast generation**: Go from blog to podcast in under 2 minutes (OpenAI tested).
* **🎧 Streamlit interface**: A simple and intuitive user experience.


---
## 2. Project Structure

<img width="881" height="200" alt="image" src="https://github.com/user-attachments/assets/108ae7e7-2d65-434c-8852-8cb708420596" />

---
## 3. Setup & Installation

### 1. Clone the repo

```bash
git clone https://github.com/nithishravuvari/BlogCast-Blog_to_Podcast_Agent
cd BlogCast-Blog_to_Podcast_Agent
```

### 2. Create a virtual environment
```bash
python -m venv envi_blog
source envi_blog/bin/activate    # macOS/Linux
envi_blog\Scripts\activate       # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup API keys
- Create a .env file in the project root:
```bash
OPENAI_API_KEY=your_openai_key
ELEVEN_LABS_API_KEY=your_elevenlabs_key
```

- If you’re using Ollama Mistral, make sure Ollama is installed and the mistral model is pulled:

```bash
ollama pull mistral
```


---
## 4. Usage

#### Run the app with:

```bash
streamlit run app.py
```

#### Then open the Streamlit interface in your browser and:

- Paste a blog URL
- Select a podcast voice
- Choose an LLM provider (OpenAI or Ollama)
- Generate your podcast 🎧

---
## 5. Screenshots
**🔹 OpenAI Output**
  <img width="995" height="624" alt="image" src="https://github.com/user-attachments/assets/8d3b8afb-f8cf-4de3-a225-8a76a554a6a3" />
  <img width="963" height="599" alt="image" src="https://github.com/user-attachments/assets/8eb543c7-af78-48b0-9272-821044beccf9" />

**🔹 Ollama Mistral Output**
<img width="997" height="571" alt="image" src="https://github.com/user-attachments/assets/2bb9cb41-f8eb-476a-b841-f55def30024f" />
<img width="1145" height="515" alt="image" src="https://github.com/user-attachments/assets/7d4c2e32-4262-4eee-9dc8-f906560c4449" />
<img width="1108" height="319" alt="image" src="https://github.com/user-attachments/assets/baeb7ef1-9edd-4db7-a30f-cf05101237ac" />


