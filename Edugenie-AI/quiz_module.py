from ai_client import generate_text
def generate_quiz(topic: str, number_of_questions: int = 5) -> str:
    number_of_questions = max(1, min(number_of_questions, 10))

    prompt = f"""
Create {number_of_questions} multiple-choice quiz questions
for a student learning this topic: {topic}

For each question:
- Give four options labelled A, B, C, and D.
- Clearly show the correct answer.
- Add a one-sentence explanation.

Keep the questions beginner-friendly.
"""
    return generate_text(prompt)