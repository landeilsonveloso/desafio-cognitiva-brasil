from mistralai import Mistral
import os
from dotenv import load_dotenv

load_dotenv()

client = Mistral(
    api_key=os.getenv("API_KEY_MISTRALAI")
)

def mistralAi(prompt):
    response = client.chat.complete(
        model= "mistral-large-latest",
        messages = [
            {
                "role": "user",
                "content": prompt,
            },
        ]
    )
    
    return response.choices[0].message.content
