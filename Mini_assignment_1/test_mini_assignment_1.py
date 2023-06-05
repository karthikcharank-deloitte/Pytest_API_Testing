import pytest
import requests


def test_check_status_code_equals_200(api_url):
    response = requests.get(f"{api_url}/v1/airlines")
    print(response.status_code)
    assert response.status_code == 200


@pytest.fixture()
def api_url():
    return "https://api.instantwebtools.net"
