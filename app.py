import uvicorn

from fastapi import FastAPI
from database import dependencies, orm
from src.account.http import account
from src.transaction.http import transaction


def create_app() -> FastAPI:
    app = FastAPI(title="Simple Transaction", docs_url="/v1/docs")

    app.include_router(account.router)
    app.include_router(transaction.router)

    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
