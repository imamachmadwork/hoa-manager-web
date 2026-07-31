import time

import allure
import pytest

# Discovered from the Rental Applications page's network traffic: the
# "Undecided" and "All Applications" tabs both call this endpoint,
# distinguished by filters.statuses (0 = Undecided, [] = no filter/all).
APPLICATIONS_SEARCH_PATH = "/pms/applications/search"
APPLICATIONS_PATH = "/pms/applications"
PROSPECTS_PATH = "/pms/prospects"

UNDECIDED_STATUS = 0

META_KEYS = {
    "totalApplications",
    "pendingApplications",
    "approvedApplications",
    "rejectedApplications",
    "currentPage",
    "perPage",
    "total",
}


def _search_applications(api_client, org_api_base, property_id, statuses, limit=10):
    return api_client.post(
        f"{org_api_base}{APPLICATIONS_SEARCH_PATH}",
        json={
            "sortDirection": "desc",
            "sortActive": "date",
            "limit": limit,
            "page": 1,
            "property": property_id,
            "filters": {"statuses": statuses},
        },
    )


@pytest.mark.smoke
def test_undecided_applications_search_returns_expected_shape(
    api_client, authenticated_session, default_property_id
):
    response = _search_applications(
        api_client, authenticated_session["org_api_base"], default_property_id, [UNDECIDED_STATUS]
    )

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body["data"], list)
    assert META_KEYS.issubset(body["meta"].keys())


@pytest.mark.smoke
def test_all_applications_search_returns_expected_shape(api_client, authenticated_session, default_property_id):
    response = _search_applications(api_client, authenticated_session["org_api_base"], default_property_id, [])

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body["data"], list)
    assert META_KEYS.issubset(body["meta"].keys())


def test_applications_search_rejects_unauthenticated_request(api_client, credentials):
    creds = credentials("liberty")
    org_api_base = api_client.resolve_org_api_base(creds["organization_slug"])

    response = _search_applications(api_client, org_api_base, property_id="irrelevant", statuses=[])

    assert response.status_code == 401


@pytest.fixture
def created_application(
    api_client, authenticated_session, default_property_id, default_unit_id, default_assigned_user_id
):
    """Creates a real prospect + rental application via the API, for tests
    that verify list/detail data rather than the creation flow itself.
    """
    org_api_base = authenticated_session["org_api_base"]
    unique_suffix = int(time.time() * 1000)
    email = f"qa.api.rental+{unique_suffix}@example.com"

    prospect_response = api_client.post(
        f"{org_api_base}{PROSPECTS_PATH}",
        json={
            "name": "QA API",
            "nameLast": f"Applicant {unique_suffix}",
            "nameCompany": "",
            "employerTitle": "",
            "notes": "",
            "email": email,
            "contactPhone": "",
            "password": "Roam@2025",
        },
    )
    prospect_response.raise_for_status()
    prospect = prospect_response.json()

    application_response = api_client.post(
        f"{org_api_base}{APPLICATIONS_PATH}",
        json={
            "userId": prospect["id"],
            "propertyId": default_property_id,
            "unitId": default_unit_id,
            "moveInDate": "2026-12-01",
            "assignedUserId": default_assigned_user_id,
            "hasFee": False,
            "fee": 0,
            "firstName": prospect["name"],
            "lastName": prospect["nameLast"],
            "email": email,
            "tenants": [{"id": prospect["id"], "tenantOrder": 1}],
        },
    )
    application_response.raise_for_status()
    return application_response.json()


@pytest.mark.smoke
def test_created_application_detail_matches_submitted_values(
    api_client, authenticated_session, created_application, default_unit_id, default_assigned_user_id
):
    org_api_base = authenticated_session["org_api_base"]

    response = api_client.get(f"{org_api_base}{APPLICATIONS_PATH}/{created_application['id']}")

    assert response.status_code == 200
    body = response.json()
    assert body["email"] == created_application["email"]
    assert body["unitId"] == default_unit_id
    assert body["assignedUserId"] == default_assigned_user_id
    assert body["statusName"] == "Pending"
    assert body["moveInDate"].startswith("2026-12-01")


# --- Known bugs -------------------------------------------------------------
# See tests/e2e/test_leasing_rental_application.py for the section-level
# explanation of why these assert correct behavior and are marked known_bug.


@pytest.mark.known_bug
@allure.tag("known-bug")
def test_created_application_appears_in_search(
    api_client, authenticated_session, default_property_id, created_application
):
    """Known bug (issue #8): a just-created application isn't returned by the
    search endpoint. Reproduced across 4 separate runs (3 local, 1 CI) - see
    reports/bug-reports/backend/leasing-rental-application-api.md. Looks like
    a read-lag/indexing gap between POST /pms/applications (write) and
    POST /pms/applications/search (read), not a pagination issue: this widens
    the page size to 100, well above this org's accumulated application count
    at the time each run failed.
    """
    response = _search_applications(
        api_client, authenticated_session["org_api_base"], default_property_id, [], limit=100
    )

    assert response.status_code == 200
    ids = [row["id"] for row in response.json()["data"]]
    assert created_application["id"] in ids
