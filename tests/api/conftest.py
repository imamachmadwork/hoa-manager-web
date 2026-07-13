import pytest

from clients.api_client import ApiClient


@pytest.fixture
def api_client():
    with ApiClient() as client:
        yield client
