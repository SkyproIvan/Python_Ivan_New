import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# ВАЖНО: замените на свои данные подключения!
DB_URL = "postgresql://postgres:123@localhost:5432/QA Ivan"

engine = create_engine(DB_URL)
Session = scoped_session(sessionmaker(bind=engine))

@pytest.fixture(scope="function")
def db_session():
    # Подключение к БД
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)
    yield session  # Передаём сессию в тест

    # Очистка данных после теста (откат транзакции)
    session.close()
    transaction.rollback()
    connection.close()