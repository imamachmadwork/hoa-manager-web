import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def home_page(page):
    from pages.home_page import HomePage

    return HomePage(page)
