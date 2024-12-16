from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4
from datetime import datetime

Base = declarative_base()


def generate_uuid():
    return str(uuid4())


class Account(Base):
    __tablename__ = "account"

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    number = Column(String, nullable=False, unique=True)
    balance = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, nullable=False, default=datetime.now)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "number": self.number,
            "balance": self.balance,
        }


class TransactionLog(Base):
    __tablename__ = "transaction_log"

    id = Column(String, primary_key=True, default=generate_uuid)
    sender_number = Column(String, nullable=False)
    receiver_number = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)

    def to_dict(self):
        return {
            "id": self.id,
            "sender_number": self.sender_number,
            "receiver_number": self.receiver_number,
            "amount": self.amount,
        }
