from mistralai import Mistral
import os
from dotenv import load_dotenv

load_dotenv()

client = Mistral(
    api_key=os.getenv("MISTRALAI_API_KEY")
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
