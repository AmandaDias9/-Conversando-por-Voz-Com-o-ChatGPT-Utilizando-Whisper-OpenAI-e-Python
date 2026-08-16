# 🎙️ Conversando por Voz com o ChatGPT

> Assistente de voz utilizando **Whisper**, **OpenAI**, **Python** e **gTTS**.

Projeto desenvolvido como parte de um desafio da **DIO**, com o objetivo de criar um assistente capaz de receber perguntas por voz, transformar áudio em texto, gerar uma resposta com Inteligência Artificial e reproduzir essa resposta em áudio.

---

## 🚀 Sobre o Projeto

O sistema integra tecnologias de **Speech-to-Text** e **Text-to-Speech**, permitindo uma interação por voz com Inteligência Artificial.

O funcionamento acontece da seguinte maneira:

🎤 **Usuário fala**

⬇️

🧠 **Whisper transforma o áudio em texto**

⬇️

💬 **ChatGPT processa a pergunta e gera uma resposta**

⬇️

🔊 **gTTS transforma a resposta em áudio**

---

## 🛠️ Tecnologias Utilizadas

- 🐍 Python
- 🎙️ OpenAI Whisper
- 🤖 OpenAI API
- 🔊 Google Text-to-Speech (gTTS)
- 🎧 PortAudio
- 🔐 Variáveis de ambiente com `.env`
- 🐙 Git e GitHub

---

## 📂 Estrutura do Projeto

```text
voice-chatgpt/
│
├── main.py
├── requirements.txt
├── .env.example
│
└── src/
    ├── record_audio.py
    ├── transcribe.py
    ├── chat.py
    └── speak.py
