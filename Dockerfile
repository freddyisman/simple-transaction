FROM python:3.11-slim

WORKDIR /app

COPY ./database /app/database
COPY ./domain /app/domain
COPY ./service /app/service
COPY ./test /app/test

COPY poetry.lock pyproject.toml alembic.ini app.py .env /app/

RUN pip install poetry
RUN poetry lock --no-update
RUN poetry install

ENV APP_MODULE=app:app
ENV PORT=8000

CMD poetry run alembic downgrade base && poetry run alembic upgrade head && poetry run pytest test && poetry run uvicorn $APP_MODULE --host 0.0.0.0 --port $PORT
