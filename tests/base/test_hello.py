import pytest

def test_app_says_hello(client):
    """ tests app says hello /api/hello """
    response = client.fetch(
        method="get",
        path="hello"
    )
    assert response.status_code == 200
    assert response.json["message"] == "hello app name 📊"