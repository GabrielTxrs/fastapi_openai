from fastapi import FastAPI
from utils import gerarBoletimOcorrencia
from transcribe import run_whisperx_cmd

app = FastAPI()

# audio/audio1.wav 
# audio/audio2.wav
# audio/roubo-1.mp3
# audio/roubo-2.mp3

@app.post("/gerar_bo/{caminhoAudio}")
async def gerarBo(caminhoAudio: str):
    transcricao = run_whisperx_cmd("audio/"+caminhoAudio)
    return gerarBoletimOcorrencia(transcricao)
    

