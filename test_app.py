import pytest
from app import app

def test_index():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Username' in response.data

def test_login_success():
    client = app.test_client()
    response = client.post('/login', data={'username': 'user', 'password': 'password'})
    
    assert response.status_code == 302
    assert response.location.endswith('/dashboard')
    response = client.get('/dashboard')
    assert b'Welcome to your dashboard!' in response.data

def test_login_failure():
    client = app.test_client()
    response = client.post('/login', data={'username': 'user', 'password': 'wrongpassword'})
    assert response.status_code == 200
    assert b'Invalid credentials' in response.data
