import pytest


@pytest.fixture(scope="function")
def setup():
    print("Started Testcase: test_api_call_with_different_params()")
    yield
    print("Completed Testcase: test_api_call_with_different_params()")
