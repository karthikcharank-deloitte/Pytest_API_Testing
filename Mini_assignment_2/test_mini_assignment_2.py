import pytest
import requests

json_content_1 = {'id': 1, 'name': 'Sri Lankan Airways', 'country': 'Sri Lanka',
                  'logo': 'https://upload.wikimedia.org/wikipedia/en/thumb/9/9b/Qatar_Airways_Logo.svg/sri_lanka.png',
                  'slogan': 'From Sri Lanka', 'head_quaters': 'Katunayake, Sri Lanka',
                  'website': 'www.srilankaairways.com', 'established': '1990'
                  }

json_content_2 = {'__v': 0,
                  '_id': '6465dc71c3e3936a547989b0',
                  'airline': [{'__v': 0,
                               '_id': '64648884b0653e3d6dc9a8d2',
                               'country': 'VN',
                               'established': '1999',
                               'head_quaters': 'FLy, Sky',
                               'id': 1999,
                               'logo': 'https://upload.wikimedia.org/wikipedia/en/thumb/9/9b/Qatar_Airways_Logo.svg/sri_lanka.png',
                               'name': 'My Airways',
                               'slogan': 'Fly with me',
                               'website': 'www.myairways.com'}],
                  'name': 'Nhi',
                  'trips': 250
                  }


def test_verify_json_contents_1(api_url):
    response = requests.get(f"{api_url}/v1/airlines/1")
    response_body = response.json()
    print(response_body)
    assert response_body == json_content_1


def test_verify_json_contents_2():
    response = requests.get("https://api.instantwebtools.net/v1/passenger?page=0&size=2")
    response_body = response.json()
    print(response_body["data"][1])
    assert response_body["data"][1] == json_content_2


@pytest.fixture()
def api_url():
    return "https://api.instantwebtools.net"
