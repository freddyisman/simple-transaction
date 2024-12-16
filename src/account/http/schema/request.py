from pydantic import BaseModel
from typing import Optional


class CreateAccountRequest(BaseModel):
    name: str
    number: str
    balance: Optional[int] = 0
