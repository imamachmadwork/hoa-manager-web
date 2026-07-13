import re

import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_sign_in_redirects_to_dashboard(sign_in_page, credentials):
    creds = credentials("liberty")

    sign_in_page.load()
    sign_in_page.sign_in(
        organization_id=creds["organization_id"],
        email=creds["email"],
        password=creds["password"],
    )

    expect(sign_in_page.page).to_have_url(
        re.compile(rf"^https://{re.escape(creds['organization_id'])}\.roamstay\.com/overview"),
        timeout=15000,
    )
