from ai_client import generate_text


def recommend_learning_path(topic: str) -> str:
    prompt = f"""
Create a beginner-friendly learning path for this topic: {topic}

Include:
1. Prerequisites
2. Learning topics in the correct order
3. A small practice task for each stage
4. A final mini-project idea

Use clear headings and simple language.
"""
    return