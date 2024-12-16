from fastapi.routing import APIRouter

from database.dependencies import SessionLocal
from src.transaction.http.schema import request, response
from src.transaction.service import transaction as transaction_service

router = APIRouter(prefix="/transaction", tags=["Transaction"])


@router.post(
    "",
    responses={
        201: {"model": response.CreateTransactionResponse},
        404: {"model": response.ErrorResponse},
    },
    status_code=201,
)
def create_transaction(request: request.CreateTransactionRequest):
    db_session = SessionLocal()
    try:
        transaction = transaction_service.create_transaction(db_session, request)
    except Exception as e:
        return response.ErrorResponse(message=str(e))
    else:
        return response.CreateTransactionResponse(
            data=response.TransactionData(**transaction),
        )


@router.get(
    "/{transaction_id}",
    responses={
        200: {"model": response.GetTransactionResponse},
        404: {"model": response.ErrorResponse},
    },
    status_code=200,
)
def get_transaction_by_transaction_id(transaction_id: str):
    db_session = SessionLocal()
    try:
        transaction = transaction_service.get_transaction_by_transaction_id(
            db_session, transaction_id
        )
    except Exception as e:
        return response.ErrorResponse(message=str(e))
    else:
        return response.GetTransactionResponse(
            data=response.TransactionData(**transaction),
        )


@router.get(
    "",
    response_model=response.ListTransactionResponse,
    status_code=200,
)
def list_transaction():
    db_session = SessionLocal()
    transactions = transaction_service.list_transaction(db_session)
    return response.ListTransactionResponse(
        data=[response.TransactionData(**transaction) for transaction in transactions],
    )
