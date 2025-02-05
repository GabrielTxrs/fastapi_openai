import os
from openai import OpenAI

api_key = os.getenv['OPEN_AI_API_KEY']

client = OpenAI(api_key=api_key)

  # Add your OpenAI API key here

def generate_description(input):
    messages = [
        {"role": "system",
         "content": """As a Product Description Generator, Generate multi paragraph rich text product description with emojis from the information provided to you' \n"""},
    ]

    messages.append({"role": "user", "content": f"{input}"})
    completion = client.chat.completions.create(model="gpt-4o-mini",
    messages=messages)
    reply = completion.choices[0].message.content
    return reply



# curl https://api.openai.com/v1/chat/completions \
#   -H "Content-Type: application/json" \
#   -H "Authorization: Bearer 
#   -d '{
#     "model": "gpt-4o-mini",
#     "store": true,
#     "messages": [
#       {"role": "user", "content": "write a haiku about ai"}
#     ]
#   }'