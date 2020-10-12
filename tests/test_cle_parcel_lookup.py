import pytest
import requests
import requests_mock

class MockResponse:
    status_code = 400
    
    @staticmethod
    def json():
        return {'mock_key': 'mock_response'}

def test_index(client):
    response = client.get('/')
    assert b"Parcel Details" in response.data

def test_parcel_valid(client):
    with client.get('/parcel/100-11-222') as resp:
        assert resp.status_code == 200

def test_parcel_invalid_parcel_string(client):
    with client.get('/parcel/abcdef') as resp:
        assert resp.status_code == 400
        assert b'does not conform to format' in resp.data

def test_parcel_invalid_neocando_response(client, requests_mock, monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()
    monkeypatch.setattr(requests, "get", mock_get)
    with client.get('/parcel/100-11-222') as resp:
        assert resp.status_code == 400
        assert b'Invalid response code returned for parcel' in resp.data
