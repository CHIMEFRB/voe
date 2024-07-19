import pytest
from sanic import Sanic
from frbvoe.server import create

@pytest.fixture
def app():
    return create()


def test_create_app():
    app = create()
    assert isinstance(app, Sanic)
    assert app.name == "frbvoe"


def test_server_startup(app):
    request, response = app.test_client.get("/")
    assert response.status == 200
    assert response.text == "Hello, World!"


def test_server_shutdown(app):
    request, response = app.test_client.get("/shutdown")
    assert response.status == 200
    assert response.text == "Server shutting down..."