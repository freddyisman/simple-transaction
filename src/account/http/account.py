from fastapi.routing import APIRouter

from database.dependencies import SessionLocal
from src.account.http.schema import request, response
from src.account.service import account as account_service

router = APIRouter(prefix="/account", tags=["Account"])


@router.post(
    "",
    responses={
        201: {"model": response.CreateAccountResponse},
        404: {"model": response.ErrorResponse},
    },
    status_code=201,
)
def create_account(request: request.CreateAccountRequest):
    db_session = SessionLocal()
    try:
        account = account_service.create_account(db_session, request)
    except Exception as e:
        return response.ErrorResponse(message=str(e))
    else:
        return response.CreateAccountResponse(
            data=response.AccountData(**account),
        )


@router.get(
    "/{account_number}",
    responses={
        200: {"model": response.GetAccountResponse},
        404: {"model": response.ErrorResponse},
    },
    status_code=200,
)
def get_account_by_account_number(account_number: str):
    db_session = SessionLocal()
    try:
        account = account_service.get_account_by_account_number(
            db_session, account_number
        )
    except Exception as e:
        return response.ErrorResponse(message=str(e))
    else:
        return response.GetAccountResponse(
            data=response.AccountData(**account),
        )


@router.get(
    "",
    response_model=response.ListAccountResponse,
    status_code=200,
)
def list_account():
    db_session = SessionLocal()
    accounts = account_service.list_account(db_session)
    return response.ListAccountResponse(
        data=[response.AccountData(**account) for account in accounts],
    )
