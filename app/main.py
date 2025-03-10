from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from utils import gerarBoletimOcorrencia
from transcribe import run_whisperx_cmd
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return HTMLResponse(open("index.html").read())

@app.post("/gerar-bo")
async def gerar_bo(audio_file: UploadFile = File(...)):
    file_location = f"audio/{audio_file.filename}"
    with open(file_location, "wb") as file:
        file.write(await audio_file.read())

    transcricao = run_whisperx_cmd(file_location)
    return FileResponse(gerarBoletimOcorrencia(transcricao))

@app.post("/gerar-bo-por-caminho/{caminhoAudio}")
async def gerarBo(caminhoAudio: str):
    transcricao = run_whisperx_cmd("audio/"+caminhoAudio)
    return gerarBoletimOcorrencia(transcricao)

# @app.post("/gerar-bo-2")
# async def gerar_bo_2(audio_file: UploadFile = File(...)):
#     file_location = f"audio/{audio_file.filename}"
#     with open(file_location, "wb") as file:
#         file.write(await audio_file.read())

#     # transcricao = run_whisperx_cmd(file_location)
#     # md_file_path = gerarBoletimOcorrencia(transcricao)
#     file_name = "boletim_ocorrencia_10_19_53.md"
#     app.mount("/boletins", StaticFiles(directory="static"), name="static")
#     md_file_url = os.path.join("boletins", file_name)
#     return {"url": md_file_url}