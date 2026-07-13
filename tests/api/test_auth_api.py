import pytest

# Discovered from the sign-in page's network traffic: the frontend first
# resolves the organization's own API host via the directory API
# (api_client.resolve_org_api_base), then posts credentials there. Mirrors
# tests/e2e/test_sign_in.py but hits the API directly instead of driving
# the browser.
LANDING_AUTHENTICATE_PATH = "/pms/users/landing-authenticate"


@pytest.mark.smoke
def test_sign_in_returns_session_token(api_client, credentials):
    creds = credentials("liberty")
    org_api_base = api_client.resolve_org_api_base(creds["organization_slug"])

    response = api_client.post(
        f"{org_api_base}{LANDING_AUTHENTICATE_PATH}",
        json={
            "language": "en",
            "organization": creds["organization_slug"],
            "email": creds["email"],
            "password": creds["password"],
            "mfaCode": "",
        },
    )

    assert response.status_code == 200
    assert "accessToken" in response.json()


def test_sign_in_rejects_invalid_password(api_client, credentials):
    creds = credentials("liberty")
    org_api_base = api_client.resolve_org_api_base(creds["organization_slug"])

    response = api_client.post(
        f"{org_api_base}{LANDING_AUTHENTICATE_PATH}",
        json={
            "language": "en",
            "organization": creds["organization_slug"],
            "email": creds["email"],
            "password": "wrong-password",
            "mfaCode": "",
        },
    )

    assert response.status_code == 401
    assert response.json()["code"] == "INVALID_CREDENTIALS"
