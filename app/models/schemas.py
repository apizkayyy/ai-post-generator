from pydantic import BaseModel, Field
from typing import Literal


class PostRequest(BaseModel):
    product_name: str = Field(..., description="Product name to promote")
    description: str | None = Field(
        default=None,
        description="Product details"
    )

    genre: Literal[
        "storytelling",
        "review",
        "educational",
        "problem_solution",
        "comparison",
        "promotion"
    ]

    tone: Literal[
        "casual",
        "professional",
        "funny",
        "emotional",
        "persuasive"
    ]

    platform: Literal[
        "Threads",
        "Instagram",
        "TikTok",
        "Shoppee"
    ] = "Threads"

    thread_count: int = Field(
        default=3,
        ge=1,
        le=6
    )


class ThreadPost(BaseModel):
    number: int
    content: str


class GeneratedPost(BaseModel):
    hooks: list[str]
    posts: list[ThreadPost]
    cta: str


class PostResponse(BaseModel):
    result: GeneratedPost