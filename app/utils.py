import os
from openai import OpenAI
from transcribe import run_whisperx_cmd
from datetime import datetime

api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

def gerarBoletimOcorrencia(input):
  print(input)
  completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "system", "content": "Você é um sistema gerador de Boletins de Ocorrência da Polícia de Sergipe."+
          "Você deve ouvir um áudio e a partir das informações dele, criar um boletim de ocorrência com a data do crime,"+ 
          "o endereço, a descrição do acontecimento e os envolvidos. Se houverem informações no áudio, "+
          "adicione uma descrição dos envolvidos. Você não deve dar sugestões. Você deve usar somente informações do "+
          "áudio para gerar o boletim de ocorrência. Seja objetivo e claro. Admita que a transcrição pode conter erros e tente corrigí-los."},
        {
            "role": "user",
            "content": f"{input}"
        }
    ]
  )
  response = completion.choices[0].message.content

  # Salvando a resposta num arquivo .md
  if not os.path.exists("boletins"):
    os.makedirs("boletins")
  formatted_time = datetime.now().strftime("%d_%H_%M")
  file_name = f"boletim_ocorrencia_{formatted_time}.md"
  file_path = os.path.join("boletins", file_name)

  with open(file_path, "w") as file:
      file.write(response)
  
  print(f"Boletim salvo em {file_name}")
  return file_path