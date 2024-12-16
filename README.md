# FastAPI Microservice Simple Transaction Service


## API Endpoints

1. `POST /account`: Create account
2. `GET /account/:account_number`: Get account by account number
3. `GET /account`: List all created accounts
4. `POST /transaction`: Create transaction
5. `GET /transaction/:transaction_id`: Get transaction by transaction id
6. `GET /transaction`: List all created transactions


## Tech Stack, Frameworks & Authentication

- Python with FastAPI framework
- PostgreSQL database with Alembic migration for database management
- Docker for containerization with Docker Compose for multiple containers


## How to run

1.  Start the service by running below command:
    ```
    sudo docker compose up
    ```


## How to test

1. Start the service first, then access http://0.0.0.0:8000/v1/docs for Swagger API testing.


## Database Schema

```
class Account(Base):
    __tablename__ = "account"

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    number = Column(String, nullable=False, unique=True)
    balance = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, nullable=False, default=datetime.now)


class TransactionLog(Base):
    __tablename__ = "transaction_log"

    id = Column(String, primary_key=True, default=generate_uuid)
    sender_number = Column(String, nullable=False)
    receiver_number = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
```
