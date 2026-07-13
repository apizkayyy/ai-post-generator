from openai import AsyncOpenAI

from app.core.config import settings


client = AsyncOpenAI(
    api_key=settings.OPENAI_API_KEY
)

POST_SCHEMA = {
    "type": "object",

    "properties": {

        "hooks": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },


        "posts": {

            "type": "array",

            "items": {

                "type": "object",

                "properties": {

                    "number": {
                        "type": "integer"
                    },

                    "content": {
                        "type": "string"
                    }

                },

                "required": [
                    "number",
                    "content"
                ],

                "additionalProperties": False
            }
        },


        "cta": {
            "type": "string"
        }

    },


    "required": [
        "hooks",
        "posts",
        "cta"
    ],


    "additionalProperties": False
}



async def generate(prompt:str):


    response = await client.responses.create(

        model=settings.OPENAI_MODEL,


        instructions=
        """
        Anda adalah content creator affiliate Malaysia.
        Hasilkan content Threads dalam Bahasa Melayu.
        """,


        input=prompt,


        max_output_tokens=settings.MAX_TOKENS,


        text={

            "format": {

                "type": "json_schema",

                "name": "affiliate_post",

                "strict": True,

                "schema": POST_SCHEMA

            }

        }

    )


    return response.output_parsed