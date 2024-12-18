from pydantic import BaseModel
from typing import List
from src.transaction.model.entity import TransactionData


class CreateTransactionResponse(BaseModel):
    data: TransactionData
    status: int = 201
    message: str = "Transaction created successfully"


class GetTransactionResponse(BaseModel):
    data: TransactionData
    status: int = 200
    message: str = "Transaction retrieved successfully"


class ListTransactionResponse(BaseModel):
    data: List[TransactionData]
    status: int = 200
    message: str = "List of transactions retrieved successfully"


class ErrorResponse(BaseModel):
    status: int = 404
    message: str = "Not Found"
