import os

# One entry per organization. Add a new key here when a new organization
# needs sign-in coverage, then set its <ORG>_EMAIL / <ORG>_PASSWORD pair
# in .env (see .env.example).
CREDENTIALS = {
    "liberty": {
        "organization_id": "liberty",
        "email": os.environ.get("LIBERTY_EMAIL"),
        "password": os.environ.get("LIBERTY_PASSWORD"),
    },
}


def get_credentials(organization_id: str) -> dict:
    try:
        return CREDENTIALS[organization_id]
    except KeyError:
        raise KeyError(f"No credentials configured for organization '{organization_id}'")
