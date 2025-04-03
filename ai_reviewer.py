import ollama

def review_text(text: str, criteria: str) -> str:
    prompt = f"Berdasarkan kriteria '{criteria}', analisis teks berikut dan berikan review detail: {text}"
    response = ollama.generate(model="llama3", prompt=prompt)
    return response['response']