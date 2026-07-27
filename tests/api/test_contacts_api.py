import time

import pytest

# Discovered from the Contacts module's network traffic (one request per
# sidebar section). Customer Accounts, Vendors, and Prospects are scoped to
# a single `property`; Homeowners/Tenants and Employees are scoped to a
# `properties` array instead; Developers is org-wide (no property scoping
# at all) - each helper below mirrors exactly what the live UI sends.
CUSTOMER_ACCOUNTS_SEARCH_PATH = "/pms/customer-accounts/search"
USERS_SEARCH_PATH = "/pms/users/search"
VENDORS_SEARCH_PATH = "/pms/vendors/search"
GROUPS_SEARCH_PATH = "/pms/groups/search"
EMPLOYEES_SEARCH_PATH = "/pms/employees/search"
PROSPECTS_SEARCH_PATH = "/pms/prospects/search"
PROSPECTS_PATH = "/pms/prospects"

PAGE_META_KEYS = {
    "total",
    "per_page",
    "current_page",
    "last_page",
    "first_page",
    "first_page_url",
    "last_page_url",
    "next_page_url",
    "previous_page_url",
}


def _search_customer_accounts(api_client, org_api_base, property_id):
    return api_client.post(
        f"{org_api_base}{CUSTOMER_ACCOUNTS_SEARCH_PATH}",
        json={
            "page": 1,
            "limit": 10,
            "sort": "name",
            "order": "asc",
            "filters": {
                "name": None,
                "address": None,
                "generation": None,
                "totalBalanceFrom": None,
                "totalBalanceTo": None,
            },
            "property": property_id,
        },
    )


def _search_users(api_client, org_api_base, property_id, role):
    return api_client.post(
        f"{org_api_base}{USERS_SEARCH_PATH}",
        json={
            "page": 1,
            "limit": 10,
            "sort": "name",
            "order": "asc",
            "filters": {"name": None, "address": None, "contact": None, "portalStatuses": []},
            "property": property_id,
            "properties": [property_id],
            "roles": [role],
        },
    )


def _search_vendors(api_client, org_api_base, property_id):
    return api_client.post(
        f"{org_api_base}{VENDORS_SEARCH_PATH}",
        json={
            "page": 1,
            "limit": 10,
            "sort": "name",
            "order": "asc",
            "filters": {
                "name": None,
                "contact": None,
                "vendorType": None,
                "countUsersFrom": None,
                "countUsersTo": None,
                "countPropertiesFrom": None,
                "countPropertiesTo": None,
                "totalBalanceFrom": None,
                "totalBalanceTo": None,
            },
            "property": property_id,
            "withCredentials": True,
        },
    )


def _search_developers(api_client, org_api_base):
    return api_client.post(
        f"{org_api_base}{GROUPS_SEARCH_PATH}",
        json={
            "limit": 10,
            "order": "asc",
            "page": 1,
            "role": "developer",
            "sort": "name",
            "filters": {"name": None, "contact": None},
        },
    )


def _search_employees(api_client, org_api_base, property_id):
    return api_client.post(
        f"{org_api_base}{EMPLOYEES_SEARCH_PATH}",
        json={
            "page": 1,
            "limit": 10,
            "sort": "name",
            "order": "asc",
            "filters": {
                "name": None,
                "contact": None,
                "subRoleName": None,
                "countPropertiesFrom": None,
                "countPropertiesTo": None,
                "lastActivityAtFrom": None,
                "lastActivityAtTo": None,
            },
            "properties": [property_id],
            "withCredentials": True,
        },
    )


def _search_prospects(api_client, org_api_base, property_id, limit=10):
    return api_client.post(
        f"{org_api_base}{PROSPECTS_SEARCH_PATH}",
        json={
            "sortDirection": "desc",
            "sortActive": "date",
            "limit": limit,
            "page": 1,
            "property": property_id,
            "filters": {},
        },
    )


@pytest.mark.smoke
def test_customer_accounts_search_returns_expected_shape(api_client, authenticated_session, default_property_id):
    response = _search_customer_accounts(api_client, authenticated_session["org_api_base"], default_property_id)

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body["data"], list)
    assert PAGE_META_KEYS.issubset(body["meta"].keys())


def test_customer_accounts_search_rejects_unauthenticated_request(api_client, credentials):
    creds = credentials("liberty")
    org_api_base = api_client.resolve_org_api_base(creds["organization_slug"])

    response = _search_customer_accounts(api_client, org_api_base, property_id="irrelevant")

    assert response.status_code == 401


@pytest.mark.smoke
def test_customer_account_detail_matches_search_result(api_client, authenticated_session, default_property_id):
    search_response = _search_customer_accounts(
        api_client, authenticated_session["org_api_base"], default_property_id
    )
    search_response.raise_for_status()
    first_account = search_response.json()["data"][0]

    detail_response = api_client.get(
        f"{authenticated_session['org_api_base']}/pms/customer-accounts/{first_account['id']}"
    )

    assert detail_response.status_code == 200
    body = detail_response.json()
    assert body["id"] == first_account["id"]
    assert body["name"] == first_account["name"]


@pytest.mark.smoke
def test_homeowners_search_returns_expected_shape(api_client, authenticated_session, default_property_id):
    response = _search_users(api_client, authenticated_session["org_api_base"], default_property_id, role="owner")

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body["data"], list)
    assert PAGE_META_KEYS.issubset(body["meta"].keys())


@pytest.mark.smoke
def test_homeowner_detail_matches_search_result(api_client, authenticated_session, default_property_id):
    """Homeowners and Tenants share the same /pms/users/search endpoint
    (see _search_users), but the detail page navigates to /pms/users/{id} -
    the same detail endpoint the UI's HomeownerDetailPage hits on row click
    (see pages/homeowner_detail_page.py)."""
    search_response = _search_users(api_client, authenticated_session["org_api_base"], default_property_id, role="owner")
    search_response.raise_for_status()
    data = search_response.json()["data"]
    assert data, "expected at least one homeowner under the default property"
    first_owner = data[0]

    detail_response = api_client.get(f"{authenticated_session['org_api_base']}/pms/users/{first_owner['id']}")

    assert detail_response.status_code == 200
    body = detail_response.json()
    assert body["id"] == first_owner["id"]
    assert body["name"] == first_owner["name"]


@pytest.mark.smoke
def test_tenants_search_returns_expected_shape(api_client, authenticated_session, default_property_id):
    # The live Liberty org has 0 tenants under its default property - assert
    # the shape rather than a non-empty result, matching the E2E empty-state
    # coverage in test_contacts.py.
    response = _search_users(api_client, authenticated_session["org_api_base"], default_property_id, role="tenant")

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body["data"], list)
    assert PAGE_META_KEYS.issubset(body["meta"].keys())


def test_users_search_rejects_unauthenticated_request(api_client, credentials):
    creds = credentials("liberty")
    org_api_base = api_client.resolve_org_api_base(creds["organization_slug"])

    response = _search_users(api_client, org_api_base, property_id="irrelevant", role="owner")

    assert response.status_code == 401


@pytest.mark.smoke
def test_vendors_search_returns_expected_shape(api_client, authenticated_session, default_property_id):
    response = _search_vendors(api_client, authenticated_session["org_api_base"], default_property_id)

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body["data"], list)
    assert PAGE_META_KEYS.issubset(body["meta"].keys())


def test_vendors_search_rejects_unauthenticated_request(api_client, credentials):
    creds = credentials("liberty")
    org_api_base = api_client.resolve_org_api_base(creds["organization_slug"])

    response = _search_vendors(api_client, org_api_base, property_id="irrelevant")

    assert response.status_code == 401


@pytest.mark.smoke
def test_vendor_detail_matches_search_result(api_client, authenticated_session, default_property_id):
    """Vendor Details navigates to GET /pms/vendors/{groupId}/{propertyId} -
    unlike Customer Accounts/Homeowners, this response is scoped per
    vendor-property association, so its own `id` is that association's id,
    not the vendor's. The search result's `id` (the vendor/group id)
    reappears as the detail response's `groupId` instead - confirmed via
    live network capture of the UI's row-click navigation (see
    pages/vendor_detail_page.py)."""
    search_response = _search_vendors(api_client, authenticated_session["org_api_base"], default_property_id)
    search_response.raise_for_status()
    data = search_response.json()["data"]
    assert data, "expected at least one vendor under the default property"
    first_vendor = data[0]

    detail_response = api_client.get(
        f"{authenticated_session['org_api_base']}/pms/vendors/{first_vendor['id']}/{default_property_id}"
    )

    assert detail_response.status_code == 200
    body = detail_response.json()
    assert body["groupId"] == first_vendor["id"]
    assert body["name"] == first_vendor["name"]


@pytest.mark.smoke
def test_developers_search_returns_expected_shape(api_client, authenticated_session):
    response = _search_developers(api_client, authenticated_session["org_api_base"])

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body["data"], list)
    assert PAGE_META_KEYS.issubset(body["meta"].keys())


def test_developers_search_rejects_unauthenticated_request(api_client, credentials):
    creds = credentials("liberty")
    org_api_base = api_client.resolve_org_api_base(creds["organization_slug"])

    response = api_client.post(
        f"{org_api_base}{GROUPS_SEARCH_PATH}",
        json={"limit": 10, "order": "asc", "page": 1, "role": "developer", "sort": "name", "filters": {}},
    )

    assert response.status_code == 401


@pytest.mark.smoke
def test_developer_detail_matches_search_result(api_client, authenticated_session):
    """Developer Details navigates to GET /pms/groups/{id} - unlike every
    other Contacts detail endpoint above, the response wraps the record in a
    single-element `group` array (`{"group": [{...}]}`) instead of returning
    it directly, confirmed via a direct API probe of the live Liberty org
    (see pages/developer_detail_page.py)."""
    search_response = _search_developers(api_client, authenticated_session["org_api_base"])
    search_response.raise_for_status()
    data = search_response.json()["data"]
    assert data, "expected at least one developer in this org"
    first_developer = data[0]

    detail_response = api_client.get(f"{authenticated_session['org_api_base']}/pms/groups/{first_developer['id']}")

    assert detail_response.status_code == 200
    body = detail_response.json()
    detail = body["group"][0]
    assert detail["id"] == first_developer["id"]
    assert detail["name"] == first_developer["name"]


@pytest.mark.smoke
def test_employees_search_returns_expected_shape(api_client, authenticated_session, default_property_id):
    response = _search_employees(api_client, authenticated_session["org_api_base"], default_property_id)

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body["data"], list)
    assert PAGE_META_KEYS.issubset(body["meta"].keys())


def test_employees_search_rejects_unauthenticated_request(api_client, credentials):
    """Unlike /pms/prospects/search (see test_prospects_search_rejects_unauthenticated_request
    below), /pms/employees/search correctly 401s with no Authorization header -
    confirmed via a direct API probe of the live Liberty org."""
    creds = credentials("liberty")
    org_api_base = api_client.resolve_org_api_base(creds["organization_slug"])

    response = _search_employees(api_client, org_api_base, property_id="irrelevant")

    assert response.status_code == 401


@pytest.mark.smoke
def test_employee_detail_matches_search_result(api_client, authenticated_session, default_property_id):
    """Employee Details navigates to GET /pms/users/{id} - the same detail
    endpoint HomeownerDetailPage's row-click hits (see
    test_homeowner_detail_matches_search_result above) - even though the
    search endpoint (/pms/employees/search) is distinct from Homeowners' own
    (/pms/users/search). Confirmed via a direct API probe of the live
    Liberty org (see pages/employee_detail_page.py)."""
    search_response = _search_employees(api_client, authenticated_session["org_api_base"], default_property_id)
    search_response.raise_for_status()
    data = search_response.json()["data"]
    assert data, "expected at least one employee under the default property"
    first_employee = data[0]

    detail_response = api_client.get(f"{authenticated_session['org_api_base']}/pms/users/{first_employee['id']}")

    assert detail_response.status_code == 200
    body = detail_response.json()
    assert body["id"] == first_employee["id"]
    assert body["name"] == first_employee["name"]


@pytest.mark.smoke
def test_prospects_search_returns_expected_shape(api_client, authenticated_session, default_property_id):
    response = _search_prospects(api_client, authenticated_session["org_api_base"], default_property_id)

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body["data"], list)
    assert PAGE_META_KEYS.issubset(body["meta"].keys())


@pytest.mark.known_bug
def test_prospects_search_rejects_unauthenticated_request(api_client, credentials):
    """FLAG (security): unlike every other Contacts search endpoint above,
    /pms/prospects/search does not enforce authentication at all when given
    a real property id - a request with no Authorization header returns 200
    with actual prospect PII (name, email, ...), not 401. An invalid/made-up
    property id does correctly 422 first (masking the gap unless you already
    know a real property id), which is what made this easy to miss. Marked
    known_bug per this repo's convention (see pyproject.toml/README): asserts
    the correct expected behavior and is expected to fail until fixed
    upstream, without blocking the main suite."""
    creds = credentials("liberty")
    org_api_base = api_client.resolve_org_api_base(creds["organization_slug"])

    response = _search_prospects(api_client, org_api_base, property_id="12613aac-76b8-4d64-a6ca-c388ff1cd438")

    assert response.status_code == 401


@pytest.fixture
def created_prospect(api_client, authenticated_session):
    """Creates a real prospect via the API (same endpoint/shape as
    tests/api/test_leasing_rental_application_api.py's created_application
    fixture), for verifying it surfaces in the Contacts > Prospects search
    rather than testing the creation flow itself."""
    org_api_base = authenticated_session["org_api_base"]
    unique_suffix = int(time.time() * 1000)
    email = f"qa.api.contacts+{unique_suffix}@example.com"

    response = api_client.post(
        f"{org_api_base}{PROSPECTS_PATH}",
        json={
            "name": "QA API",
            "nameLast": f"Contact {unique_suffix}",
            "nameCompany": "",
            "employerTitle": "",
            "notes": "",
            "email": email,
            "contactPhone": "",
            "password": "Roam@2025",
        },
    )
    response.raise_for_status()
    return response.json()


@pytest.mark.smoke
def test_created_prospect_appears_in_contacts_search(
    api_client, authenticated_session, default_property_id, created_prospect
):
    # This org has accumulated many prospects from repeated test runs, so a
    # small page size (matching the UI's default of 10) isn't guaranteed to
    # include a freshly created record - widen it for this assertion.
    response = _search_prospects(api_client, authenticated_session["org_api_base"], default_property_id, limit=200)

    assert response.status_code == 200
    ids = [row["id"] for row in response.json()["data"]]
    assert created_prospect["id"] in ids
