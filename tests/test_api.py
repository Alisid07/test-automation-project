import requests
import pytest

def test_get_request():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        json_response = response.json()
        assert json_response.get("id") == 1
    except requests.RequestException as e:
        pytest.fail(f"API request failed: {e}")
