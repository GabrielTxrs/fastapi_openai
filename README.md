# Configuração do Whisperx num ambiente Ubuntu 24.04.2

### 1. Create Python3.10 environment

```
conda create --name whisperx python=3.10
```

```
conda activate whisperx
```

### 2. Instalar ctranslate2
Talvez esse passo não sejam necessários caso você não possua GPU NVIDIA, mas eu os executei.
```
pip install ctranslate2
```

```
docker pull ghcr.io/opennmt/ctranslate2:latest-ubuntu20.04-cuda11.2
```

```
docker run --rm ghcr.io/opennmt/ctranslate2:latest-ubuntu20.04-cuda11.2 --help
```

### 3. Instalar PyTorch para Linux e Windows # CPU Only
Caso possua GPU NVIDIA, use o comando recomendado 
(```conda install pytorch==2.0.0 torchaudio==2.0.0 pytorch-cuda=11.8 -c pytorch -c nvidia```)
https://pytorch.org/get-started/previous-versions/#v200

```
conda install pytorch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 cpuonly -c pytorch
```

### 4. Instalar WhisperX

Stable Release (recomendado)

```
pip install whisperx
```

### 5. Instalando ffmpeg, rust e setuptools-rust
Instruções da openAI: https://github.com/openai/whisper#setup.


```
sudo apt update && sudo apt install ffmpeg
```

```
pip install rust
```

```
pip install setuptools-rust
```

### 6. Adicionando o token(read) do Hugging Face

```
export HF_TOKEN=SEU_TOKEN_DO_HUGGING_FACE
```

### 7. Testando a funcionalidade
```
whisperx caminho_audio --diarize --compute_type float32 --language Portuguese
```

### 8. Rodar a FastAPI

```
cd app && uvicorn main:app
```