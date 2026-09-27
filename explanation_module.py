from ai_client import generate_text
def explain_concept(topic: str) -> str:
    prompt = f"""
You are EduGenie, a patient tutor.
Explain the following concept to a beginner.

Include:
1. A simple definition
2. A step-by-step explanation
3. One easy example
4. A short recap

Topic:
{topic}
"""
    return generate_text(prompt)