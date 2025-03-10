from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from utils import gerarBoletimOcorrencia
from transcribe import run_whisperx_cmd
import os
import io

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return HTMLResponse(open("index.html").read())

@app.post("/gerar-bo-por-caminho/{caminhoAudio}")
async def gerarBo(caminhoAudio: str):
    transcricao = run_whisperx_cmd("audio/"+caminhoAudio)
    return gerarBoletimOcorrencia(transcricao)

@app.post("/gerar-bo")
async def gerar_bo_2(audio_file: UploadFile = File(...)):
    file_location = f"audio/{audio_file.filename}"
    with open(file_location, "wb") as file:
        file.write(await audio_file.read())

    transcricao = run_whisperx_cmd(file_location)
    boletim_content = gerarBoletimOcorrencia(transcricao)

    return StreamingResponse(io.BytesIO(boletim_content.encode()), media_type="text/markdown", headers={"Content-Disposition": "attachment; filename=boletim.md"})