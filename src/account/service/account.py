from sqlalchemy.orm import Session

from database import orm
from src.account.model import entity

from typing import Dict, Any, List


def create_account(
    session: Session, account_data: entity.AccountData
) -> Dict[str, Any]:
    account = orm.Account(
        name=account_data.name,
        number=account_data.number,
        balance=account_data.balance,
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
