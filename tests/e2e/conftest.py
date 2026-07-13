import pytest


@pytest.fixture
def home_page(page):
    from pages.home_page import HomePage

    return HomePage(page)


@pytest.fixture
def sign_in_page(page):
    from pages.sign_in_page import SignInPage

    return SignInPage(page)
