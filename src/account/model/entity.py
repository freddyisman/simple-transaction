from pydantic import BaseModel


class AccountData(BaseModel):
    name: str
    number: str
    balance: int
