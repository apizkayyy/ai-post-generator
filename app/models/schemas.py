from pydantic import BaseModel
from typing import Optional

class PostRequest(BaseModel):
    product_name:str
    description:Optional[str]=None
    genre:str
    thread_count:int=2

class ThreadPost(BaseModel):
    number:int
    content:str

class GeneratedPost(BaseModel):
    hooks:list[str]
    posts:list[ThreadPost]
    cta:str



class PostResponse(BaseModel):

    result:GeneratedPost