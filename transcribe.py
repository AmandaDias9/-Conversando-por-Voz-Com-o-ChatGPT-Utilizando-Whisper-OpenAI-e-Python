"""Transcreve áudio para texto usando o Whisper (OpenAI), localmente."""

import whisper

# Carregado uma única vez e reutilizado entre chamadas (evita recarregar o modelo).
_model = None


def _get_model(model_size: str = "small"):
    global _model
    if _model is None:
        print(f"🧠 Carregando modelo Whisper '{model_size}'...")
        _model = whisper.load_model(model_size)
    return _model


def transcribe(audio_path: str, language: str = "pt", model_size: str = "small") -> str:
    """Transcreve o arquivo de áudio em `audio_path` para texto.

    `language` define o idioma esperado (ex: 'pt', 'en', 'es').
    `model_size` pode ser tiny, base, small, medium ou large
    (modelos maiores são mais precisos, porém mais lentos).
    """
    model = _get_model(model_size)
    result = model.transcribe(audio_path, fp16=False, language=language)
    text = result["text"].strip()
    print(f"📝 Transcrição: {text}\n")
    return text
