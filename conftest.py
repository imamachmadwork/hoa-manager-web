import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def home_page(page):
    from pages.home_page import HomePage

    return HomePage(page)


@pytest.fixture
def sign_in_page(page):
    from pages.sign_in_page import SignInPage

    return SignInPage(page)


@pytest.fixture
def credentials():
    from credentials import get_credentials

    return get_credentials
