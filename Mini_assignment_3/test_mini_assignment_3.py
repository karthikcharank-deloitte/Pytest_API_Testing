import pytest
import requests

request_body = {
    "name": "Roopas Doe",
    "trips": 200,
    "airline": 128116
}

put_input = {
    "name": "Roopa",
    "trips": 200,
    "airline": 128116
    }


def test_post_request(api_url):
    response = requests.post(f"{api_url}/v1/passenger", data=request_body)
    response_body = response.json()
    assert response_body["name"] == "Roopas Doe"
    assert response_body["trips"] == 200
    assert response_body["airline"][0]["id"] == 128116


def test_put_request(api_url):
    response = requests.put(f"{api_url}/v1/passenger/6476d994fdbfa156498e9ae1", data=put_input)
    response_body = response.json()
    print(response_body)
    assert response.status_code == 200
    assert response_body == {'message': 'Passenger data put successfully completed.'}
    response = requests.get(f"{api_url}/v1/passenger/6476d994fdbfa156498e9ae1")
    updated_response = response.json()
    assert updated_response["name"] == "Roopa"
    print(updated_response["name"])


def test_delete_request(api_url):
    response = requests.delete(f"{api_url}/v1/passenger/646495f6f50535e8d633e220")
    response_body = response.json()
    print(response_body)
    assert response.status_code == 200
    assert response_body == {'message': 'Passenger data deleted successfully.'}


@pytest.fixture()
def api_url():
    return "https://api.instantwebtools.net"
