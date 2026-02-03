import pytest
from app import app

## UNIT TESTING WITH PYTEST

@pytest.fixture
def client():
    app.config('TESTING') = True
    with app.test_client() as client: ## CREATE A FAKE HTTP CLIENT FOR THE TEST
        yield client ## RETURN A VALUE BUT NOT CLOSE THE FUNCTION

## BASIC TEST FOR STATUS CODE

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_default(client):
    response = client.get('/default')
    assert response.status_code == 200

def test_variable(client):
    response = client.get('/variable')
    assert response.status_code == 200

def test_if(client):
    response = client.get('/if')
    assert response.status_code == 200

def test_for(client):
    response = client.get('/for')
    assert response.status_code == 200

## TEST CONTENT
def test_variable_content(client):
    response = client.get('/variable')
    assert b'pabloSNGULAR' in response.data

## REDIRECTIONS TEST
def test_choice_variable_redirect(client):
    response = client.get('/choice/variable')
    assert response.status_code == 302
    assert '/variable' in response.headers['Location']

def test_choice_variable_redirect(client):
    response = client.get('/choice/if')
    assert response.status_code == 302
    assert '/if' in response.headers['Location']

def test_choice_variable_redirect(client):
    response = client.get('/choice/for')
    assert response.status_code == 302
    assert '/for' in response.headers['Location']
