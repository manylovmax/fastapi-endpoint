from typing import Union

from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    text: Union[str, None] = None


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int

    class Config:
        orm_mode = True
