from openrouter import OpenRouter
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

with OpenRouter(api_key=api_key) as client:
    response = client.chat.send(
        model="openai/gpt-5",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": "What is the meaning of life?"
            }
        ],
    )

    print(response.choices[0].message.content)