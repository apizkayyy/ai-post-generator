import json
import httpx

from app.core.config import settings

async def generate(prompt: str):

    async with httpx.AsyncClient() as client:
        response = await client.post(

            f"{settings.OLLAMA_URL}/api/generate",

            json={

                "model": settings.OLLAMA_MODEL,

                "prompt": prompt,

                "format": "json",

                "stream": False,

                "options": {

                    "temperature": settings.TEMPERATURE,

                    "num_predict": settings.MAX_TOKENS

                }

            }

        )

    response.raise_for_status()

    data = response.json()

    content = data["response"]

    return json.loads(content)