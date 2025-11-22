from pydantic import BaseModel

class CategoryCreate(BaseModel):
    name: str
    is_global: bool = False
    user_id: int | None = None

    orm_mode = True
