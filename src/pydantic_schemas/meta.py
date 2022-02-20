from pydantic import BaseModel


class User(BaseModel):
    pagination: dict

    total: int
    pages: int
    page: int
    limit: int
    links: dict