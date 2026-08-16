"""Ponto de entrada: conversa por voz com o ChatGPT.

Fluxo: 🎤 grava -> 🧠 Whisper transcreve -> 💬 ChatGPT responde -> 🔊 gTTS fala.
"""

import argparse
from dotenv import load_dotenv

from src.record_audio import record
from src.transcribe import transcribe
from src.chat import ask_chatgpt
from src.speak import speak


def main():
    parser = argparse.ArgumentParser(description="Converse por voz com o ChatGPT.")
    parser.add_argument("--seconds", type=int, default=5, help="Duração da gravação em segundos.")
    parser.add_argument("--language", type=str, default="pt", help="Código do idioma (ex: pt, en, es).")
    parser.add_argument("--whisper-model", type=str, default="small", help="Tamanho do modelo Whisper.")
    parser.add_argument("--gpt-model", type=str, default="gpt-4o-mini", help="Modelo do ChatGPT a usar.")
    args = parser.parse_args()

    load_dotenv()  # carrega OPENAI_API_KEY do arquivo .env

    audio_path = record(seconds=args.seconds)
    question = transcribe(audio_path, language=args.language, model_size=args.whisper_model)

    if not question:
        print("⚠️  Não entendi nada. Tente novamente falando mais perto do microfone.")
        return

    answer = ask_chatgpt(question, model=args.gpt_model)
    speak(answer, language=args.language)


if __name__ == "__main__":
    main()
