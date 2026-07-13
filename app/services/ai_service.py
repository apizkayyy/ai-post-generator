from app.core.config import settings

from app.services.openai_service import generate as openai_generate
from app.services.ollama_service import generate as ollama_generate

async def generate(prompt:str):

    if settings.AI_PROVIDER == "openai":
        return await openai_generate(
            prompt
        )

    elif settings.AI_PROVIDER == "ollama":
        return await ollama_generate(
            prompt
        )

    else:
        raise Exception(
            f"Unsupported AI provider: {settings.AI_PROVIDER}"
        )