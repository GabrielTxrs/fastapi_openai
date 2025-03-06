from fastapi import FastAPI
from pydantic import BaseModel
from utils import gerarBo
from transcribe import transcribeAudio
app = FastAPI()

@app.get("/ok")
async def ok_endpoint():
    return {"message": "ok"}

@app.get("/hello")
async def hello_endpoint(name: str = 'World'):
    return {"message": f"Hello, {name}!"}

@app.post("/gerar_bo")
async def gerarBo(caminhoAudio: str):
    transcricao = transcribeAudio(caminhoAudio)
    print(transcricao)
    resposta = await gerarBo(transcricao)
    print(resposta)
