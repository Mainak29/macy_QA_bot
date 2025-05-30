import openai
from config import TOGETHER_API_KEY

openai.api_key = TOGETHER_API_KEY
openai.api_base = "https://api.together.xyz/v1"  # Note: 'api_base' for <1.0.0

def ask_question(question, model="mistralai/Mixtral-8x7B-Instruct-v0.1", temperature=0.7):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful & polite assistant. And your name is Macy"},
                {"role": "user", "content": question}
            ],
            temperature=temperature
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"

