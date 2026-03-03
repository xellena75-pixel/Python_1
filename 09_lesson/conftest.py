import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

#  строка подключения
DB_URL = "postgresql+psycopg2://postgres:123@localhost:5432/mydatabase"

Base = declarative_base()


# Описываем сущность Студент здесь, чтобы она была доступна везде
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    subject = Column(String)


@pytest.fixture(scope="session")
def engine():
    _engine = create_engine(DB_URL)
    Base.metadata.drop_all(_engine)  # Очистка старого мусора перед сессией
    Base.metadata.create_all(_engine)  # Создание таблицы
    yield _engine
    Base.metadata.drop_all(_engine)  # Удаление таблицы после всех тестов


@pytest.fixture
def db_session(engine):
    connection = engine.connect()
    transaction = connection.begin()
    session_factory = sessionmaker(bind=connection)
    session = session_factory()

    yield session

    session.close()
    transaction.rollback()  # ГАРАНТИРУЕТ УДАЛЕНИЕ ДАННЫХ после каждого теста
    connection.close()

