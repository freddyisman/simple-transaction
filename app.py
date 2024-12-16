import uvicorn

from fastapi import FastAPI
from database import dependencies, orm
from service import service
from domain import request, response

app = FastAPI(title="Simple Transaction", docs_url="/v1/docs")

orm.Base.metadata.create_all(bind=dependencies.engine)


@app.post(
    "/account",
    response_model=response.CreateAccountResponse,
    status_code=201,
)
def create_account(request: request.CreateAccountRequest):
    db_session = dependencies.SessionLocal()
    account = service.create_account(db_session, request)
    resp = response.CreateAccountResponse(
        data=response.AccountData(**account),
    )
    return resp


@app.get(
    "/account/{account_number}",
    response_model=response.GetAccountResponse,
    status_code=200,
)
def get_account_by_account_number(account_number: str):
    db_session = dependencies.SessionLocal()
    account = service.get_account_by_account_number(db_session, account_number)
    resp = response.GetAccountResponse(
        data=response.AccountData(**account),
    )
    return resp


@app.get(
    "/account",
    response_model=response.ListAccountResponse,
    status_code=200,
)
def list_account():
    db_session = dependencies.SessionLocal()
    accounts = service.list_account(db_session)
    resp = response.ListAccountResponse(
        data=[response.AccountData(**account) for account in accounts],
    )
    return resp


@app.post(
    "/transaction",
    response_model=response.CreateTransactionResponse,
    status_code=201,
)
def create_transaction(request: request.CreateTransactionRequest):
    db_session = dependencies.SessionLocal()
    transaction = service.create_transaction(db_session, request)
    resp = response.CreateTransactionResponse(
        data=response.TransactionData(**transaction),
    )
    return resp


@app.get(
    "/transaction/{transaction_id}",
    response_model=response.GetTransactionResponse,
    status_code=200,
)
def get_transaction_by_transaction_id(transaction_id: str):
    db_session = dependencies.SessionLocal()
    transaction = service.get_transaction_by_transaction_id(db_session, transaction_id)
    resp = response.GetTransactionResponse(
        data=response.TransactionData(**transaction),
    )
    return resp


@app.get(
    "/transaction",
    response_model=response.ListTransactionResponse,
    status_code=200,
)
def list_transaction():
    db_session = dependencies.SessionLocal()
    transactions = service.list_transaction(db_session)
    resp = response.ListTransactionResponse(
        data=[response.TransactionData(**transaction) for transaction in transactions],
    )
    return resp


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
