"""Sintetiza texto em áudio usando o Google Text-to-Speech (gTTS) e reproduz."""

from gtts import gTTS
from playsound import playsound


def speak(text: str, language: str = "pt", output_path: str = "response_audio.mp3") -> str:
    """Converte `text` em áudio, salva em `output_path` e reproduz.

    Retorna o caminho do arquivo de áudio gerado.
    """
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_path)
    print(f"🔊 Reproduzindo resposta ({output_path})...")
    playsound(output_path)
    return output_path
