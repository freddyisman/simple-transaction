from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import dotenv

dotenv.load_dotenv(verbose=True)
DATABASE_URL = os.getenv("DATABASE_URL", "")


class DB:
    def __init__(self, db_url: str) -> None:
        engine = create_engine(db_url)
        self.engine = engine
        self.session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def get_session(self):
        return self.session()


db_service = DB(DATABASE_URL)


def get_database():
    return db_service
