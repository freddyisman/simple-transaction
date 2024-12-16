from pydantic import BaseModel
from typing import List, Optional


class CreateAccountRequest(BaseModel):
    name: str
    number: str
    balance: Optional[int] = 0


class CreateTransactionRequest(BaseModel):
    sender_number: str
    receiver_number: str
    amount: int
