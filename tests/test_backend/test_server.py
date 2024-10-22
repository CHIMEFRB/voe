import pytest
from sanic import response

from frbvoe.server import create


@pytest.fixture
def app():
    app = create("test_sanic_app")

    @app.get("/")
    def basic(request):
        return response.text("foo")

    return app


# def test_shutdown(app):
#     request, response = app.test_client.post("/shutdown")
#     assert request.method.lower() == "post"
#     assert response.status == 200
#     assert response.body == "Server shutting down..."
