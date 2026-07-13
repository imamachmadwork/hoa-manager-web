import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_home_page_loads(home_page):
    home_page.load()
    assert "Roamstay" in home_page.title()


@pytest.mark.smoke
def test_home_page_shows_get_started_cta(home_page):
    home_page.load()
    expect(home_page.get_started_link).to_be_visible()
