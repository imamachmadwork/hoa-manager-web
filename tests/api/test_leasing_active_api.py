import pytest

# Discovered from the Active Leases page's network traffic: the "Pending"
# and "All Active Leases" tabs both call this endpoint, distinguished only
# by filters.statuses (0 = Pending, 1 = Active).
LEASES_SEARCH_PATH = "/pms/leases/search"

PENDING_STATUS = 0
ACTIVE_STATUS = 1

META_KEYS = {
    "totalLeases",
    "pendingLeases",
    "inProgressLeases",
    "activeLeases",
    "closedLeases",
    "resignRequiredLeases",
    "currentPage",
    "perPage",
    "total",
}


def _search_leases(api_client, org_api_base, property_id, statuses):
    return api_client.post(
        f"{org_api_base}{LEASES_SEARCH_PATH}",
        json={
            "sortDirection": "desc",
            "sortActive": "date",
            "limit": 10,
            "page": 1,
            "property": property_id,
            "filters": {"statuses": statuses},
        },
    )


@pytest.mark.smoke
def test_pending_leases_search_returns_expected_shape(api_client, authenticated_session, default_property_id):
    response = _search_leases(
        api_client, authenticated_session["org_api_base"], default_property_id, [PENDING_STATUS]
    )

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body["data"], list)
    assert META_KEYS.issubset(body["meta"].keys())


@pytest.mark.smoke
def test_active_leases_search_returns_expected_shape(api_client, authenticated_session, default_property_id):
    response = _search_leases(
        api_client, authenticated_session["org_api_base"], default_property_id, [ACTIVE_STATUS]
    )

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body["data"], list)
    assert META_KEYS.issubset(body["meta"].keys())


def test_leases_search_rejects_unauthenticated_request(api_client, credentials):
    creds = credentials("liberty")
    org_api_base = api_client.resolve_org_api_base(creds["organization_slug"])

    response = _search_leases(api_client, org_api_base, property_id="irrelevant", statuses=[ACTIVE_STATUS])

    assert response.status_code == 401
