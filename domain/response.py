from pydantic import BaseModel
from typing import Dict, Any, List


class AccountData(BaseModel):
    name: str
    number: str
    balance: int


class CreateAccountResponse(BaseModel):
    data: AccountData
    status: int = 201
    message: str = "Account created successfully"


class GetAccountResponse(BaseModel):
    data: AccountData
    status: int = 200
    message: str = "Account retrieved successfully"


class ListAccountResponse(BaseModel):
    data: List[AccountData]
    status: int = 200
    message: str = "List of accounts retrieved successfully"


class TransactionData(BaseModel):
    id: str
    sender_number: str
    receiver_number: str
    amount: int


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
