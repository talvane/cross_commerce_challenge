from fastapi.testclient import TestClient

from api.main import app


client = TestClient(app)


def test_get_numbers():
    response = client.get('/numbers')
    assert response.status_code == 200
