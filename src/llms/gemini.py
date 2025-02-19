from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def gemini(prompt):
    response = client.models.generate_content(
        model = "gemini-2.0-flash",
        contents = prompt
    )
    
    return response.text
