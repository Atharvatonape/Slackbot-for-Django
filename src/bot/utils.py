import os
from openai import OpenAI
import helpers

OPENAI_API_KEY = helpers.config('OPEANAI_API_KEY', default=None, cast=str)

def get_open_ai_client():
    return  OpenAI(
        # This is the default and can be omitted
        api_key=OPENAI_API_KEY,
    )

def chat_with_openai(message, model="gpt-3.5-turbo", raw=False):
    client = get_open_ai_client()
    response = client.chat.completions.create(
        messages=[
           {
                "role": "system",
                "content": "You are an amazing code assistant",
            },
            {
                "role": "user",
                "content": message,
            }
        ],
        model=model,
    )
    if raw:
        return response
    return response.choices[0].message.content