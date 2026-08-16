# 🎙️ Conversa por Voz com ChatGPT (Whisper + gTTS)

Sistema que une **Speech-to-Text** (Whisper) e **Text-to-Speech** (gTTS) para
permitir uma conversa por voz, multi-idioma, com o ChatGPT.

Fluxo: 🎤 você fala → 🧠 Whisper transcreve → 💬 ChatGPT responde → 🔊 gTTS fala a resposta.

## Estrutura

```
voice-chatgpt/
├── main.py                # orquestra o fluxo completo
├── requirements.txt
├── .env.example            # copie para .env e preencha sua chave
└── src/
    ├── record_audio.py     # grava áudio do microfone
    ├── transcribe.py       # Whisper: áudio -> texto
    ├── chat.py              # ChatGPT: texto -> resposta
    └── speak.py             # gTTS: texto -> áudio
```

## Como usar

1. Clone o repositório e crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
   > No Linux pode ser necessário instalar o `ffmpeg` e o `portaudio`:
   > `sudo apt install ffmpeg portaudio19-dev`

3. Copie `.env.example` para `.env` e adicione sua chave da OpenAI:
   ```bash
   cp .env.example .env
   ```

4. Rode o projeto:
   ```bash
   python main.py --seconds 5 --language pt
   ```

## Diferenças em relação ao lab original (Colab)

- Gravação de áudio feita com **`sounddevice`** (funciona localmente, não só no navegador do Colab).
- API da OpenAI atualizada para a versão atual do SDK (`from openai import OpenAI`),
  já que `openai.ChatCompletion.create` foi descontinuado.
- Chave de API lida de variável de ambiente (`.env`), nunca hardcoded no código.
- Código modularizado em `src/` em vez de tudo em um único notebook.

## Ideias para evoluir o projeto (portfólio 😉)

- Trocar o Whisper local pela API `whisper-1`/`gpt-4o-transcribe` da OpenAI (mais rápido, sem baixar modelo).
- Detectar o idioma automaticamente em vez de fixar `language`.
- Criar interface web simples (Streamlit ou Gradio) no lugar do terminal.
- Manter histórico da conversa (lista de mensagens) para permitir contexto entre perguntas.
- Trocar o gTTS por uma voz mais natural (ex: API de TTS da OpenAI).

## Créditos

Baseado no desafio de projeto da [DIO](https://web.dio.me/) —
"Conversando Por Voz Com o ChatGPT Utilizando Whisper (OpenAI) e Python".
