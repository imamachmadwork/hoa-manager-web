import re

import pytest
from playwright.sync_api import expect

LIBERTY_OVERVIEW_URL = "https://liberty.roamstay.com/overview"
LIBERTY_OVERVIEW_URL_PATTERN = re.compile(r"^https://liberty\.roamstay\.com/overview")
LIBERTY_ACTIVE_LEASES_URL_PATTERN = re.compile(r"^https://liberty\.roamstay\.com/leasing/active")
LIBERTY_RENTAL_APPLICATIONS_URL_PATTERN = re.compile(r"^https://liberty\.roamstay\.com/leasing/rental")

# Config for the Contacts module's seven list sections, keyed by the
# sidebar's route slug. Discovered by scanning the live site's Contacts
# sidebar menu and each section's rendered <h1>; see ContactsListPage for
# what's shared across all seven.
CONTACTS_SECTIONS = {
    "customers": {
        "menu_item_name": "Customer Accounts",
        "heading_text": "All Customer Accounts",
        "url_pattern": re.compile(r"^https://liberty\.roamstay\.com/contacts/customers"),
    },
    "owners": {
        "menu_item_name": "Homeowners",
        "heading_text": "All Homeowners",
        "url_pattern": re.compile(r"^https://liberty\.roamstay\.com/contacts/owners"),
    },
    "tenants": {
        "menu_item_name": "Tenants",
        "heading_text": "All Tenants",
        "url_pattern": re.compile(r"^https://liberty\.roamstay\.com/contacts/tenants"),
    },
    "vendors": {
        "menu_item_name": "Vendors",
        "heading_text": "All Vendors",
        "url_pattern": re.compile(r"^https://liberty\.roamstay\.com/contacts/vendors"),
    },
    "developers": {
        "menu_item_name": "Developers",
        "heading_text": "All Developers",
        "url_pattern": re.compile(r"^https://liberty\.roamstay\.com/contacts/developers"),
    },
    "employees": {
        "menu_item_name": "Employees",
        "heading_text": "All Employees",
        "url_pattern": re.compile(r"^https://liberty\.roamstay\.com/contacts/employees"),
    },
    "prospects": {
        "menu_item_name": "Prospects",
        "heading_text": "All Prospects",
        "url_pattern": re.compile(r"^https://liberty\.roamstay\.com/contacts/prospects"),
    },
}


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


@pytest.fixture
def rental_application_page(authenticated_page):
    from pages.rental_application_page import RentalApplicationPage

    return RentalApplicationPage(authenticated_page)


@pytest.fixture
def add_rental_application_page(authenticated_page):
    from pages.add_rental_application_page import AddRentalApplicationPage

    return AddRentalApplicationPage(authenticated_page)


@pytest.fixture
def rental_application_detail_page(authenticated_page):
    from pages.rental_application_detail_page import RentalApplicationDetailPage

    return RentalApplicationDetailPage(authenticated_page)


@pytest.fixture
def signed_in_rental_applications_page(rental_application_page):
    """Prerequisite for leasing module tests: an already-authenticated page
    (see liberty_storage_state), navigated to Rental Applications."""
    rental_application_page.page.goto(LIBERTY_OVERVIEW_URL)
    rental_application_page.open()
    expect(rental_application_page.page).to_have_url(LIBERTY_RENTAL_APPLICATIONS_URL_PATTERN)
    return rental_application_page


@pytest.fixture
def seeded_rental_application(liberty_session_token):
    """Creates a real prospect + rental application via direct API calls
    (see tests/api/test_leasing_rental_application_api.py for the same
    pattern), so list/detail-rendering tests can assert against known
    values without driving the multi-dialog creation UI, which is flaky:
    the "Select Prospect" list doesn't refresh after adding a new prospect,
    and Escape closes the whole "Add Rental Application" dialog rather than
    just the date picker.
    """
    import time

    from clients.api_client import ApiClient

    org_api_base = liberty_session_token["org_api_base"]

    with ApiClient() as client:
        client.headers["Authorization"] = f"Bearer {liberty_session_token['session_token']}"

        property_id = client.get(f"{org_api_base}/pms/associations").json()["properties"][0]["id"]
        unit = client.get(f"{org_api_base}/pms/associations/{property_id}/units").json()["units"][0]
        assigned_user = client.post(
            f"{org_api_base}/pms/users/search-by-role-names",
            json={"roles": ["employee"], "filters": {"keyword": ""}, "propertyId": property_id},
        ).json()[0]

        unique_suffix = int(time.time() * 1000)
        email = f"qa.e2e.rental+{unique_suffix}@example.com"
        prospect = client.post(
            f"{org_api_base}/pms/prospects",
            json={
                "name": "QA E2E",
                "nameLast": f"Applicant {unique_suffix}",
                "nameCompany": "",
                "employerTitle": "",
                "notes": "",
                "email": email,
                "contactPhone": "",
                "password": "Roam@2025",
            },
        ).json()

        application = client.post(
            f"{org_api_base}/pms/applications",
            json={
                "userId": prospect["id"],
                "propertyId": property_id,
                "unitId": unit["id"],
                "moveInDate": "2026-12-01",
                "assignedUserId": assigned_user["id"],
                "hasFee": False,
                "fee": 0,
                "firstName": prospect["name"],
                "lastName": prospect["nameLast"],
                "email": email,
                "tenants": [{"id": prospect["id"], "tenantOrder": 1}],
            },
        ).json()

        # Re-fetch rather than trusting the values just submitted: the create
        # endpoint doesn't always honor unitId as sent (observed swapping to
        # a different unit under the same property), so the detail GET is
        # the only authoritative source for what was actually persisted.
        detail = client.get(f"{org_api_base}/pms/applications/{application['id']}").json()

    return {
        "application": application,
        "unit_name": detail["unit"]["name"],
        "assigned_user_name": detail["assignedUser"]["name"],
    }


@pytest.fixture(params=list(CONTACTS_SECTIONS.keys()))
def contacts_section(request):
    """Parametrizes any test that uses it to run once per Contacts sidebar
    section (see CONTACTS_SECTIONS), so a single test scans the whole module."""
    return request.param


@pytest.fixture
def signed_in_contacts_page(authenticated_page, contacts_section):
    from pages.contacts_list_page import ContactsListPage

    config = CONTACTS_SECTIONS[contacts_section]
    contacts_list_page = ContactsListPage(
        authenticated_page,
        menu_item_name=config["menu_item_name"],
        heading_text=config["heading_text"],
    )
    contacts_list_page.page.goto(LIBERTY_OVERVIEW_URL)
    contacts_list_page.open()
    expect(contacts_list_page.page).to_have_url(config["url_pattern"])
    return contacts_list_page


@pytest.fixture
def signed_in_customer_accounts_page(authenticated_page):
    """Prerequisite for Customer Accounts-specific tests (filters, row
    navigation) that don't need to run across all seven Contacts sections."""
    from pages.contacts_list_page import ContactsListPage

    config = CONTACTS_SECTIONS["customers"]
    contacts_list_page = ContactsListPage(
        authenticated_page,
        menu_item_name=config["menu_item_name"],
        heading_text=config["heading_text"],
    )
    contacts_list_page.page.goto(LIBERTY_OVERVIEW_URL)
    contacts_list_page.open()
    expect(contacts_list_page.page).to_have_url(config["url_pattern"])
    return contacts_list_page


@pytest.fixture
def customer_account_detail_page(authenticated_page):
    from pages.customer_account_detail_page import CustomerAccountDetailPage

    return CustomerAccountDetailPage(authenticated_page)
