import pytest

from app import create_app
from app.config import TestingConfig


@pytest.fixture(scope="session")
def app():
    app = create_app(TestingConfig)
    app_context = app.test_request_context()
    app_context.push()

    yield app

    app_context.pop()
