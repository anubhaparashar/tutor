# openai_utils.py
import openai
from typing import List

openai.api_key = "your_openai_api_key"  # Use environment variables in production

def ask_openai_question(text: str, question: str, history: List[dict]) -> str:
    context = " ".join([h["question"] + " " + h["answer"] for h in history])
    prompt = f"Context: {context}\n\nBook Text: {text}\n\nQuestion: {question}\n\nAnswer:"
    
    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].text.strip()
