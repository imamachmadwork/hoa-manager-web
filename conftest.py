from pathlib import Path

import allure
import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def credentials():
    from credentials import get_credentials

    return get_credentials


@pytest.fixture(scope="session")
def liberty_session_token():
    """Logs in as Liberty once per test session via direct API calls (no
    browser), shared by both tests/api and tests/e2e. The live site
    rate-limits repeated landing-authenticate calls within a short window,
    so every suite needing an authenticated API session reuses this single
    login instead of triggering its own.

    Mirrors the browser's two-step flow (see tests/api/test_auth_api.py):
    landing-authenticate returns a one-time accessToken, which
    landing-verify exchanges for the actual session token used as
    `Authorization: Bearer <token>` on every subsequent org-scoped call.
    """
    from clients.api_client import ApiClient
    from credentials import get_credentials

    creds = get_credentials("liberty")

    with ApiClient() as client:
        org_api_base = client.resolve_org_api_base(creds["organization_slug"])

        auth_response = client.post(
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

        verify_response = client.get(f"{org_api_base}/pms/users/landing-verify/{access_token}")
        verify_response.raise_for_status()
        session_token = verify_response.json()["token"]

    return {"org_api_base": org_api_base, "session_token": session_token}


def pytest_collection_modifyitems(items):
    """Auto-tag every test as frontend (tests/e2e) or backend (tests/api),
    so suites can be run/filtered independently with `pytest -m frontend`."""
    for item in items:
        parts = Path(str(item.fspath)).parts
        if "e2e" in parts:
            item.add_marker(pytest.mark.frontend)
        elif "api" in parts:
            item.add_marker(pytest.mark.backend)


@pytest.fixture(autouse=True)
def _allure_suite_labels(request):
    """Tag every test with an Allure epic (suite) and feature (layer), so the
    Allure report can be sliced by test suite or by Frontend/Backend without
    per-test decorators.

    - epic: derived from the test file name, e.g. test_sign_in.py -> "Sign In"
    - feature: "Frontend" for tests/e2e, "Backend" for tests/api
    """
    path = Path(str(request.node.fspath))
    allure.dynamic.epic(path.stem.removeprefix("test_").replace("_", " ").title())

    parts = path.parts
    if "e2e" in parts:
        allure.dynamic.feature("Frontend")
    elif "api" in parts:
        allure.dynamic.feature("Backend")
