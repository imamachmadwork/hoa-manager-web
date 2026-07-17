import pytest

from clients.api_client import ApiClient


@pytest.fixture
def api_client():
    with ApiClient() as client:
        yield client


@pytest.fixture
def authenticated_session(api_client, liberty_session_token):
    """Applies the session-wide Liberty login to this test's api_client, for
    tests that need an authenticated session rather than testing the login
    endpoint itself.
    """
    api_client.headers["Authorization"] = f"Bearer {liberty_session_token['session_token']}"
    return {"org_api_base": liberty_session_token["org_api_base"]}


@pytest.fixture
def default_property_id(api_client, authenticated_session):
    """The first association/property in the org's portfolio, used to scope
    property-level endpoints like /pms/leases/search the same way the UI's
    default (unfiltered) association context does.
    """
    response = api_client.get(f"{authenticated_session['org_api_base']}/pms/associations")
    response.raise_for_status()
    return response.json()["properties"][0]["id"]


@pytest.fixture
def default_unit_id(api_client, authenticated_session, default_property_id):
    """The first unit under the default property, used to fill required
    unit fields the same way the UI's "Select Unit" dropdown does.
    """
    response = api_client.get(
        f"{authenticated_session['org_api_base']}/pms/associations/{default_property_id}/units"
    )
    response.raise_for_status()
    return response.json()["units"][0]["id"]


@pytest.fixture
def default_assigned_user_id(api_client, authenticated_session, default_property_id):
    """The first employee eligible to be assigned to a rental application,
    the same list the UI's "Select Assigned To" dropdown is populated from.
    """
    response = api_client.post(
        f"{authenticated_session['org_api_base']}/pms/users/search-by-role-names",
        json={"roles": ["employee"], "filters": {"keyword": ""}, "propertyId": default_property_id},
    )
    response.raise_for_status()
    return response.json()[0]["id"]
