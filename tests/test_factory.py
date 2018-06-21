from medileaks import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_welcome_message(client):
    response = client.get('/home')
    assert response.data == b'Welcome to Medileaks!'