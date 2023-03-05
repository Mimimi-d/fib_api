import json
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_fib(client):
    res = client.get('/fib?n=99')
    assert res.status_code == 200
    assert json.loads(res.data) == {'result': 218922995834555169026}

def test_fib_missing_parameter(client):
    res = client.get('/fib')
    assert res.status_code == 400
    assert json.loads(res.data) == {'status': 400, 'message': 'n is required'}

def test_fib_invalid_string_parameter(client):
    res = client.get('/fib?n=abc')
    assert res.status_code == 400
    assert json.loads(res.data) == {'status': 400, 'message': 'n = abc . n must be a positive integer'}

def test_fib_invalid_negative_parameter(client):
    res = client.get('/fib?n=-1')
    assert res.status_code == 400
    assert json.loads(res.data) == {'status': 400, 'message': 'n = -1 . n must be a positive integer'}

def test_fib_invalid_float_parameter(client):
    res = client.get('/fib?n=0.1')
    assert res.status_code == 400
    assert json.loads(res.data) == {'status': 400, 'message': 'n = 0.1 . n must be a positive integer'}

def test_fib_method_not_allowed(client):
    res = client.post('/fib')
    assert res.status_code == 405
    assert json.loads(res.data) == {'status': 405, 'message': 'Method (POST) Not Allowed'}

def test_unknown_route(client):
    res = client.get('/unknown')
    assert res.status_code == 404
    assert json.loads(res.data) == {'status': 404, 'message': 'Not Found. Please '}
