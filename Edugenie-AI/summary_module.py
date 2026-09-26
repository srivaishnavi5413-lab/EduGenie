from ai_client import generate_text
def summarize_text(text: str) -> str:
    prompt = f"""
Summarize the following text for a student.

Use:
- A short paragraph
- Important points as bullets
- Simple language
- Do not add information that is not in the text

Text:
{text}
"""
    return generate_text(prompt)