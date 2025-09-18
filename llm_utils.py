import os
from openai import OpenAI as OpenAIClient
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

def chunk_text(text, max_chars=3000):
    """Split text into chunks under max_chars."""
    paragraphs = text.split("\n")
    chunks, current = [], ""
    for p in paragraphs:
        if len(current) + len(p) < max_chars:
            current += p + "\n"
        else:
            chunks.append(current.strip())
            current = p + "\n"
    if current:
        chunks.append(current.strip())
    return chunks

def summarize_with_openai(text):
    client = OpenAIClient(api_key=os.getenv("OPENAI_API_KEY"))
    chunks = chunk_text(text)
    summaries = []
    for chunk in chunks:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a podcast narrator."},
                {"role": "user", "content": f"Summarize this blog in a clear, spoken style:\n\n{chunk}"}
            ],
        )
        summaries.append(response.choices[0].message.content)
    return "\n".join(summaries)

def summarize_with_ollama(text, model="mistral"):
    llm = ChatOllama(model=model)
    chunks = chunk_text(text)
    summaries = []
    for chunk in chunks:
        prompt = ChatPromptTemplate.from_template(
            "Summarize this blog in conversational podcast style:\n\n{blog_text}"
        )
        chain = prompt | llm
        result = chain.invoke({"blog_text": chunk})
        summaries.append(result.content)
    return "\n".join(summaries)

def summarize_text(text, provider="OpenAI"):
    """Route summarization to the selected LLM provider."""
    try:
        if provider == "OpenAI":
            return summarize_with_openai(text)
        elif provider == "Ollama (Mistral)":
            return summarize_with_ollama(text)
        else:
            return "❌ Invalid LLM provider selected."
    except Exception as e:
        st.error(f"🤖 Summarization failed: {e}")
        return None
