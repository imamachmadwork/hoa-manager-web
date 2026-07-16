import pytest

from clients.api_client import ApiClient


@pytest.fixture
def api_client():
    with ApiClient() as client:
        yield client


@pytest.fixture
def authenticated_session(api_client, credentials):
    """Log in as the given organization and leave api_client carrying a
    Bearer session token, for tests that need an authenticated session
    rather than testing the login endpoint itself.

    Mirrors the browser's two-step flow (see tests/api/test_auth_api.py):
    landing-authenticate returns a one-time accessToken, which
    landing-verify exchanges for the actual session token used as
    `Authorization: Bearer <token>` on every subsequent org-scoped call.
    """
    creds = credentials("liberty")
    org_api_base = api_client.resolve_org_api_base(creds["organization_slug"])

    auth_response = api_client.post(
        f"{org_api_base}/pms/users/landing-authenticate",
        json={
            "language": "en",
            "organization": creds["organization_slug"],
            "email": creds["email"],
            "password": creds["password"],
            "mfaCode": "",
        },
    )
    auth_response.raise_for_status()
    access_token = auth_response.json()["accessToken"]

    verify_response = api_client.get(f"{org_api_base}/pms/users/landing-verify/{access_token}")
    verify_response.raise_for_status()
    session_token = verify_response.json()["token"]

    api_client.headers["Authorization"] = f"Bearer {session_token}"

    return {"org_api_base": org_api_base}


@pytest.fixture
def default_property_id(api_client, authenticated_session):
    """The first association/property in the org's portfolio, used to scope
    property-level endpoints like /pms/leases/search the same way the UI's
    default (unfiltered) association context does.
    """
    response = api_client.get(f"{authenticated_session['org_api_base']}/pms/associations")
    response.raise_for_status()
    return response.json()["properties"][0]["id"]
