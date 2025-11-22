from pydantic import BaseModel

class ExpenseCreate(BaseModel):
    category_id: int
    user_id: int | None = None
    amount: int
    description: str | None = None
    date: str

    orm_mode = True
