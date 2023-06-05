import pytest
import requests


@pytest.mark.parametrize("page, size", [(0, 10), (1, 5), (2, 3)])
def test_api_call_with_different_params(page, size, setup):
    url = "https://api.instantwebtools.net/v1/passenger"
    params = {"page": page, "size": size}
    response = requests.get(url, params=params)
    response_body = response.json()
    print(len(response_body["data"]))
    assert response.status_code == 200
    assert len(response_body["data"]) == size
