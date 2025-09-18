import os
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from openai import OpenAI as OpenAIClient

# Load API key
openai_api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text: str, provider: str = "Ollama (Mistral)") -> str:
    """Summarize text using the selected LLM provider."""
    prompt_text = f"""
    Summarize the following blog content in a clear, conversational style.
    Keep it under 2000 characters:

    {text}
    """

    try:
        if provider == "Ollama (Mistral)":
            llm = ChatOllama(model="mistral")
            prompt = ChatPromptTemplate.from_template("{blog_text}")
            chain = prompt | llm
            return chain.invoke({"blog_text": prompt_text}).content

        elif provider == "OpenAI":
            client = OpenAIClient(api_key=openai_api_key)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt_text}]
            )
            return response.choices[0].message.content.strip()

    except Exception:
        return None
