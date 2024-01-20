import app
import json
import warnings

def test_name():
    response = app.app.test_client().get('/hello')
    assert response.status_code == 200
    assert response.data == b'hello'  #return type must be same othrwise it will give error.

def test_goodbye():
    response = app.app.test_client().get('/goodbye')
    assert response.status_code == 200
    assert response.data == b'goodbye'

def test_age():
    response = app.app.test_client().get('/age')
    assert response.status_code == 200
    assert response.data == b'23'