from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_should_return_200_hello():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Olá!'}
