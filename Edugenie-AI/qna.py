from ai_client import generate_text
def answer_question(question: str) -> str:
    prompt = f"""
You are EduGenie, a friendly learning assistant.
Answer the student's question clearly and accurately.
Use simple language and examples where helpful.

Student question:
{question}
"""
    return generate_text(prompt)