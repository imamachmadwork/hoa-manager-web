import os

# One entry per organization. Add a new key here when a new organization
# needs sign-in coverage, then set its <ORG>_EMAIL / <ORG>_PASSWORD pair
# in .env (see .env.example).
CREDENTIALS = {
    "liberty": {
        "organization_id": "liberty",
        # Full slug/groupCode as returned by GET /search-organizations and
        # required by the backend's landing-authenticate "organization" field
        # (distinct from organization_id, which is just the UI search term).
        "organization_slug": "liberty-community-management-inc",
        "email": os.environ.get("LIBERTY_EMAIL"),
        "password": os.environ.get("LIBERTY_PASSWORD"),
    },
}


def get_credentials(organization_id: str) -> dict:
    try:
        return CREDENTIALS[organization_id]
    except KeyError:
        raise KeyError(f"No credentials configured for organization '{organization_id}'")
