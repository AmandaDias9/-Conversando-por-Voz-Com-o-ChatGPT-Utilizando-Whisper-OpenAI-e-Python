"""Envia o texto transcrito para o ChatGPT e retorna a resposta.

Usa o SDK atual da OpenAI (`openai>=1.0`), já que `openai.ChatCompletion.create`
foi descontinuado.
"""

import os
from openai import OpenAI

_client = None


def _get_client() -> OpenAI:
    global _client
    if _client is None:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError(
                "OPENAI_API_KEY não encontrada. Configure-a no arquivo .env."
            )
        _client = OpenAI(api_key=api_key)
    return _client


def ask_chatgpt(prompt: str, model: str = "gpt-4o-mini") -> str:
    """Envia `prompt` ao ChatGPT e retorna o texto da resposta."""
    client = _get_client()
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    reply = response.choices[0].message.content
    print(f"💬 Resposta do ChatGPT: {reply}\n")
    return reply
