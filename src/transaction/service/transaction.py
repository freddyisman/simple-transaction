from sqlalchemy.orm import Session
from sqlalchemy import text

from database import orm
from ..http.schema import request

from typing import Dict, Any, List


def create_transaction(
    session: Session, request: request.CreateTransactionRequest
) -> Dict[str, Any]:
    sender_account = (
        session.query(orm.Account)
        .filter(orm.Account.number == request.sender_number)
        .first()
    )
    receiver_account = (
        session.query(orm.Account)
        .filter(orm.Account.number == request.receiver_number)
        .first()
    )

    if not sender_account or not receiver_account:
        raise Exception("Account not found")

    session.execute(
        text(
            "SELECT create_transaction(:sender_number, :receiver_number, :transaction_amount)"
        ),
        {
            "sender_number": sender_account.number,
            "receiver_number": receiver_account.number,
            "transaction_amount": request.amount,
        },
    )

    session.commit()

    transaction = (
        session.query(orm.TransactionLog)
        .order_by(orm.TransactionLog.created_at.desc())
        .first()
    )
    return transaction.to_dict()


def get_transaction_by_transaction_id(
    session: Session, transaction_id: str
) -> Dict[str, Any]:
    transaction = (
        session.query(orm.TransactionLog)
        .filter(orm.TransactionLog.id == transaction_id)
        .first()
    )
    session.close()
    if not transaction:
        raise Exception("Transaction not found")

    return transaction.to_dict()


def list_transaction(session: Session) -> List[Dict[str, Any]]:
    transactions = session.query(orm.TransactionLog).all()
    session.close()
    return [transaction.to_dict() for transaction in transactions]
