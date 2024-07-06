from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_should_return_ok_and_hello():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá!'}


def test_root_should_return_html():
    client = TestClient(app)

    response = client.get('/html')

    assert response.status_code == HTTPStatus.OK
    assert (
        response.text
        == """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""
    )
