import speech_recognition as sr
from pydub import AudioSegment
import os

def transcribeAudio(audio_path: str) -> str:
    recognizer = sr.Recognizer()
    
    try:
        # Verificar se o arquivo de áudio existe
        if not os.path.exists(audio_path):
            return "Arquivo de áudio não encontrado."
        
        print(f"Processando o arquivo de áudio: {audio_path}")
        
        # Converter o arquivo .m4a para .wav temporariamente
        audio = AudioSegment.from_file(audio_path)
        temp_wav_path = audio_path.replace(".m4a", ".wav")
        audio.export(temp_wav_path, format="wav")
        print(f"Arquivo convertido para WAV: {temp_wav_path}")
    except Exception as e:
        return f"Erro ao converter o arquivo de áudio: {e}"
    
    try:
        with sr.AudioFile(temp_wav_path) as source:
            audio = recognizer.record(source)
        
        text = recognizer.recognize_google(audio, language="pt-BR")
        print(f"Texto transcrito: {text}")
    except sr.UnknownValueError:
        text = "Não foi possível transcrever o áudio."
    except sr.RequestError:
        text = "Erro ao se comunicar com o serviço de reconhecimento de fala."
    except Exception as e:
        text = f"Erro ao processar o arquivo de áudio: {e}"
    finally:
        # Remover o arquivo .wav temporário
        if os.path.exists(temp_wav_path):
            os.remove(temp_wav_path)
    
    return text