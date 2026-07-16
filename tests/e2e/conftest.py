import re

import pytest
from playwright.sync_api import expect

LIBERTY_OVERVIEW_URL = "https://liberty.roamstay.com/overview"
LIBERTY_OVERVIEW_URL_PATTERN = re.compile(r"^https://liberty\.roamstay\.com/overview")
LIBERTY_ACTIVE_LEASES_URL_PATTERN = re.compile(r"^https://liberty\.roamstay\.com/leasing/active")


@pytest.fixture
def home_page(page):
    from pages.home_page import HomePage

    return HomePage(page)


@pytest.fixture
def sign_in_page(page):
    from pages.sign_in_page import SignInPage

    return SignInPage(page)


@pytest.fixture(scope="session")
def liberty_storage_state(browser, base_url):
    """Signs in to Liberty once per test session and captures the resulting
    storage state (cookies/localStorage), so leasing-module tests can start
    already authenticated instead of each driving its own UI sign-in.

    The live site rate-limits repeated sign-in attempts within a short
    window, and every leasing test independently signing in was tripping
    that limit partway through a full suite run.
    """
    from credentials import get_credentials
    from pages.sign_in_page import SignInPage

    creds = get_credentials("liberty")
    context = browser.new_context(base_url=base_url)
    page = context.new_page()

    sign_in_page = SignInPage(page)
    sign_in_page.load()
    sign_in_page.sign_in(
        organization_id=creds["organization_id"],
        email=creds["email"],
        password=creds["password"],
    )
    expect(page).to_have_url(LIBERTY_OVERVIEW_URL_PATTERN, timeout=15000)

    state = context.storage_state()
    context.close()
    return state


@pytest.fixture
def authenticated_page(browser, liberty_storage_state):
    """A page pre-authenticated for Liberty, reusing the session-wide storage
    state instead of driving a fresh login."""
    context = browser.new_context(storage_state=liberty_storage_state)
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def leasing_active_page(authenticated_page):
    from pages.leasing_active_page import LeasingActivePage

    return LeasingActivePage(authenticated_page)


@pytest.fixture
def add_lease_page(authenticated_page):
    from pages.add_lease_page import AddLeasePage

    return AddLeasePage(authenticated_page)


@pytest.fixture
def signed_in_active_leases_page(leasing_active_page):
    """Prerequisite for leasing module tests: an already-authenticated page
    (see liberty_storage_state), navigated to Active Leases."""
    leasing_active_page.page.goto(LIBERTY_OVERVIEW_URL)
    leasing_active_page.open()
    expect(leasing_active_page.page).to_have_url(LIBERTY_ACTIVE_LEASES_URL_PATTERN)
    return leasing_active_page
