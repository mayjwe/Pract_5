from sqlalchemy import *
from sqlalchemy.orm import *
class DBSettings():
    @staticmethod
    def get_session():
        engine = create_engine(f"postgresql+psycopg2://postgres:vjk9597@localhost:5432/FastApi")
        return Session(bind=engine)