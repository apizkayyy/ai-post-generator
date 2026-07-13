from fastapi import APIRouter, HTTPException

from app.models.schemas import PostRequest, PostResponse
from app.services.prompt_builder import build_prompt
from app.services.ai_service import generate

router=APIRouter()

@router.post(
    "/generate",
    response_model=PostResponse
)
async def generate_post(
    request:PostRequest
):

    try:

        prompt=build_prompt(
            request
        )

        result=await generate(
            prompt
        )

        if len(result["posts"]) != request.thread_count:
            raise Exception(
                f"Expected {request.thread_count} threads "
                f"but AI returned {len(result['posts'])}"
            )

        return {
            "result":result
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )