import os

import httpx


class ApiClient(httpx.Client):
    """Thin httpx.Client wrapper for hitting the backend API directly
    (no browser), scoped to a base URL read from API_BASE_URL.

    The platform is multi-tenant: API_BASE_URL is the directory API
    (https://api.roamstay.com) used to look organizations up; each
    organization is then served from its own apiBaseUrl (e.g.
    https://api.liberty.roamstay.com), which is where auth and all other
    org-scoped endpoints actually live.
    """

    def __init__(self, **kwargs):
        base_url = os.environ.get("API_BASE_URL") or "https://api.roamstay.com"
        super().__init__(base_url=base_url, timeout=15.0, **kwargs)

    def resolve_org_api_base(self, organization_slug: str) -> str:
        response = self.get("/search-organizations", params={"q": organization_slug})
        response.raise_for_status()
        results = response.json()["results"]
        return results[0]["apiBaseUrl"]
