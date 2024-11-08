import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def create_embeddings(content: str):
    response = openai.Embedding.create(input=content, model="text-embedding-ada-002")
    return response['data'][0]['embedding']

def generate_answer(content: str):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Answer the following based on the content: {content}",
        max_tokens=150
    )
    return response.choices[0].text.strip()