from pydantic import BaseModel
from typing import Optional


class TransactionData(BaseModel):
    id: Optional[str] = None
    sender_number: str
    receiver_number: str
    amount: int
