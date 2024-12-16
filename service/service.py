import os
import json

from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import update

from database import orm
from domain import request

from typing import Dict, Optional, Any, List


def create_account(
    session: Session, request: request.CreateAccountRequest
) -> Dict[str, Any]:
    account = orm.Account(
        name=request.name,
        number=request.number,
        balance=request.balance,
    )
    session.add(account)
    session.commit()
    return account.to_dict()


def get_account_by_account_number(
    session: Session, account_number: str
) -> Dict[str, Any]:
    account = (
        session.query(orm.Account).filter(orm.Account.number == account_number).first()
    )
    session.close()
    if not account:
        raise Exception("Account not found")

    return account.to_dict()


def list_account(session: Session) -> List[Dict[str, Any]]:
    accounts = session.query(orm.Account).all()
    session.close()
    return [account.to_dict() for account in accounts]


def create_transaction(
    session: Session, request: request.CreateTransactionRequest
) -> Dict[str, Any]:
    source_account = (
        session.query(orm.Account)
        .filter(orm.Account.number == request.sender_number)
        .first()
    )
    destination_account = (
        session.query(orm.Account)
        .filter(orm.Account.number == request.receiver_number)
        .first()
    )

    if not source_account or not destination_account:
        raise Exception("Account not found")

    session.query(orm.Account).filter(
        orm.Account.id == source_account.id,
    ).update({orm.Account.balance: orm.Account.balance - request.amount})

    session.query(orm.Account).filter(
        orm.Account.id == destination_account.id,
    ).update({orm.Account.balance: orm.Account.balance + request.amount})

    transaction = orm.TransactionLog(
        sender_number=request.sender_number,
        receiver_number=request.receiver_number,
        amount=request.amount,
    )

    session.add(transaction)
    session.commit()
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
