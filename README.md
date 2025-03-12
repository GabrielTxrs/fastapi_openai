# Configuração do whisperX num ambiente Ubuntu 24.04.2

Muitos dos passos citados abaixo vem da documentação oficial do whisperX, plataforma utilizada para a transcrição e identificação de locutores, disponícel no link: (https://github.com/m-bain/whisperX).
Caso você tenha uma GPU NVIDIA e deseje rodar essa aplicação utilizando CUDA, recomendo que siga o passo a passo do whisperX, caso não possua uma GPU NVIDIA, saiba que existem métodos de rodar o CUDA em GPUs AMD, o SCALE é um desses métodos, mas existem diversos requisitos de hardware, sistemas operacionais, virtualização, etc... Caso deseje rodar essa aplicação em CPU, assim como fizemos, siga nesse tutorial.

### 1. Instalar o Conda (se necessário)

```
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```
```
source ~/miniconda3/bin/activate
```

```
conda init --all
```
Caso o conda esteja abrindo em todas as suas sessões de terminal, ex:

```
(base) nome_usuario:~/fastapi_openai $
```

Você pode desativar essa configuração do conda com o comando:

```
conda config --set auto_activate_base false
```


### 2. Criar o conda environment com Python3.10

```
conda create --name whisperx python=3.10
```

```
conda activate whisperx
```

### 3. Instalar ctranslate2

Provavelmente esse passo não é necessário caso você não possua GPU NVIDIA, mas eu executei.

```
pip install ctranslate2
```

```
docker pull ghcr.io/opennmt/ctranslate2:latest-ubuntu20.04-cuda11.2
```

```
docker run --rm ghcr.io/opennmt/ctranslate2:latest-ubuntu20.04-cuda11.2 --help
```

### 4. Instalar PyTorch, torchvision e torchaudio para Linux # CPU Only
Caso possua GPU NVIDIA, use o comando recomendado pela documentação oficial do Whisperx
(```conda install pytorch==2.0.0 torchaudio==2.0.0 pytorch-cuda=11.8 -c pytorch -c nvidia```)
https://pytorch.org/get-started/previous-versions/#v200
Caso possua GPU AMD, procure a documentação do SCALE e ROCm https://docs.scale-lang.com/

Em nosso caso, fomos pela opção cpuonly
```
conda install pytorch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 cpuonly -c pytorch
```

### 5. Instalar WhisperX

Stable Release (recomendado)

```
pip install whisperx
```

### 6. Instalando ffmpeg, rust e setuptools-rust

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

### 7. Adicione o token(read) do Hugging Face e da OpenAI

```
export OPENAI_API_KEY=SEU_TOKEN_DA_OPENAI
```
```
export HF_TOKEN=SEU_TOKEN_DO_HUGGING_FACE
```

### 8. Testando a funcionalidade (Opcional)
```
whisperx caminho_audio --diarize --compute_type float32 --language Portuguese
```

### 9. Instalar os requirements da FastAPI
```
pip install -r requirements.txt
```

### 10. Rodar a FastAPI

```
cd app && uvicorn main:app
```
Pronto, agora basta acessar o front end da fastapi em: http://127.0.0.1:8000