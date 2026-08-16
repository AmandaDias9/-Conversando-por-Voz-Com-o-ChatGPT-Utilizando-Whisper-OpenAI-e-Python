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

  Função dos arquivos
Arquivo	Função
main.py	Controla o fluxo principal da aplicação
record_audio.py	Realiza a gravação do microfone
transcribe.py	Transforma o áudio em texto utilizando Whisper
chat.py	Envia a mensagem para a OpenAI
speak.py	Converte a resposta em áudio utilizando gTTS

---
⚙️ Como Executar o Projeto
1️⃣ Clone o repositório
git clone URL-DO-SEU-REPOSITORIO

Entre na pasta:

cd voice-chatgpt
2️⃣ Crie um ambiente virtual
python -m venv venv
Windows
venv\Scripts\activate
Linux / macOS
source venv/bin/activate
3️⃣ Instale as dependências
pip install -r requirements.txt
🔑 Configuração da API

Crie um arquivo chamado:

.env

Depois adicione sua chave da OpenAI:

OPENAI_API_KEY=sua_chave_aqui

⚠️ Nunca publique sua chave da OpenAI diretamente no GitHub.

▶️ Executando

Para iniciar o projeto:

python main.py

Exemplo:

python main.py --seconds 5 --language pt

O programa irá:

🎤 Gravar sua voz;
📝 Transcrever o áudio;
🤖 Enviar a pergunta para a IA;
💬 Receber a resposta;
🔊 Reproduzir a resposta em áudio.
🌎 Suporte a Idiomas

O Whisper possui suporte para diversos idiomas, permitindo expandir o projeto para criar um assistente de voz multilíngue.

Exemplos:

🇧🇷 Português
🇺🇸 Inglês
🇪🇸 Espanhol
🇫🇷 Francês
🇮🇹 Italiano
💡 Possíveis Melhorias

Algumas funcionalidades que podem ser adicionadas futuramente:

 Criar uma interface web
 Detectar o idioma automaticamente
 Manter histórico da conversa
 Adicionar Streamlit ou Gradio
 Utilizar Text-to-Speech da OpenAI
 Criar interface semelhante a um assistente virtual
 Adicionar botão para iniciar e parar gravação
🎯 Objetivo do Projeto

Este projeto demonstra na prática conceitos relacionados a:

Inteligência Artificial Generativa;
Reconhecimento de voz;
Processamento de linguagem natural;
Conversão de texto em áudio;
Integração com APIs;
Desenvolvimento utilizando Python.

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
