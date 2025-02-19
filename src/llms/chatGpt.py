from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY_CHATGPT")
)

def chatGpt(prompt):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        store = True,
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]
        )
        
    return response.choices[0].message.content  
