from pydantic import BaseModel
from typing import List


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


class ErrorResponse(BaseModel):
    status: int = 404
    message: str = "Not Found"
