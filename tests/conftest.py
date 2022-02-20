import pytest
import requests
from configuration import SERVICE_URL2


@pytest.fixture()
def get_user():
    response = requests.get(SERVICE_URL2)
    return response
    # test_object = Response(response)
    # return test_object



