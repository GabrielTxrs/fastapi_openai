import os
from openai import OpenAI

api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

def gerarBo(input):
  completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Você é um sistema gerador de Boletins de Ocorrência da Polícia de Sergipe"+
         "você deve ouvir um áudio e a partir das informações dele, criar um boletim de ocorrência com a data do"+
         "crime, o endereço, a descrição do acontecimento e os envolvidos. "},
        {
            "role": "user",
            "content": f"{input}"
        }
    ]
  )
  return completion.choices[0].message 



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