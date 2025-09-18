import requests
from bs4 import BeautifulSoup

def scrape_blog(url: str) -> str:
    """Fetch and extract text from a webpage."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        text = "\n".join(p.get_text() for p in paragraphs)
        return text.strip()
    except requests.RequestException as e:
        return None
