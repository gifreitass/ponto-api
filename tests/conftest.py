import os
from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from config import Base, engine, get_db
from main import app

import models.ponto

@pytest.fixture(scope="session")
def test_engine():
    test_db_name = os.getenv('TEST_DB_NAME')

    if test_db_name != "ponto_db_test":
        raise ValueError("Configure TEST_DB_NAME=ponto_db_test")

    if engine.url.database == test_db_name:
        raise ValueError("O banco de desenvolvimento deve ser diferente do de testes")

    test_url = engine.url.set(database=test_db_name)

    engine_test = create_engine(
        test_url,
        pool_pre_ping=True,
    )

    Base.metadata.create_all(engine_test)

    yield engine_test

    engine_test.dispose()

@pytest.fixture(scope="function")
def client(test_engine) -> Generator[TestClient, None, None]:
    with test_engine.connect() as connection:
        transaction = connection.begin()

        db = Session(
            bind=connection,
            join_transaction_mode="create_savepoint"
        )

        def override_get_db():
            yield db

        app.dependency_overrides[get_db] = override_get_db

        try:
            with TestClient(app) as test_client:
                yield test_client
        finally:
            app.dependency_overrides.clear()
            db.close()
            transaction.rollback()