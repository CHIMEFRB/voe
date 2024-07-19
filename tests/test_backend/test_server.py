import pytest
from sanic import Sanic
from frbvoe.server import create


def test_create_app():
    app = create(name="test_create_app")
    assert isinstance(app, Sanic)
    assert app.name != "frbvoe"


def test_server_startup():
    request, response = create(name="test_server_startup").test_client.get("/")
    assert response.status == 200
    assert response.text == "Hello, World!"


def test_server_shutdown():
    request, response = create(name="test_server_shutdown").test_client.get("/shutdown")
    assert response.status == 200
    assert response.text == "Server shutting down..."