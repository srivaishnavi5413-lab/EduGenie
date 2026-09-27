import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-3.5-flash")

_client = genai.Client(api_key=API_KEY) if API_KEY else None


def generate_text(prompt: str) -> str:
    """Send a prompt to Gemini and return its text response."""

    if _client is None:
        raise RuntimeError(
            "Gemini API key is missing. Add GEMINI_API_KEY to your .env file."
        )

    response = _client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )

    answer = response.text

    if not answer:
        raise RuntimeError("Gemini returned an empty response.")

    return answer.strip()

