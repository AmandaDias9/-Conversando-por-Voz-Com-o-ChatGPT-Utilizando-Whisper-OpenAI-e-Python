"""Grava áudio do microfone usando sounddevice (funciona localmente, fora do Colab)."""

import sounddevice as sd
from scipy.io.wavfile import write

SAMPLE_RATE = 44100  # Hz


def record(seconds: int = 5, output_path: str = "request_audio.wav") -> str:
    """Grava áudio do microfone por `seconds` segundos e salva em `output_path`.

    Retorna o caminho do arquivo salvo.
    """
    print(f"🎤 Ouvindo por {seconds} segundos...\n")
    audio = sd.rec(int(seconds * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
    sd.wait()  # espera a gravação terminar
    write(output_path, SAMPLE_RATE, audio)
    print(f"✅ Áudio salvo em {output_path}\n")
    return output_path
