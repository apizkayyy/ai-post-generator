from openai import AsyncOpenAI

from app.core.config import settings
from app.models.schemas import GeneratedPost


client = AsyncOpenAI(
    api_key=settings.OPENAI_API_KEY
)


async def generate(prompt: str):

    response = await client.responses.parse(

        model=settings.OPENAI_MODEL,

        instructions="""
        Anda adalah content creator affiliate Malaysia.

        Tugas:
        - Buat content Threads yang menarik
        - Gunakan Bahasa Melayu Malaysia
        - Gunakan storytelling
        - Jangan terlalu hard selling
        - Gunakan hook yang kuat
        """,

        input=prompt,

        max_output_tokens=settings.MAX_TOKENS,

        text_format=GeneratedPost
    )


    return response.output_parsed