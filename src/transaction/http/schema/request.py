from pydantic import BaseModel
from typing import List


class CreateTransactionRequest(BaseModel):
    sender_number: str
    receiver_number: str
    amount: int
