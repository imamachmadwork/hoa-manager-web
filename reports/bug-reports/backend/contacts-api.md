# Contacts Api — Backend bugs

- Generated: 2026-07-27 18:34 UTC
- Environment: https://roamstay.com
- Failing tests: 1

## test_prospects_search_rejects_unauthenticated_request

- Status: `failed`
- Full name: `tests.api.test_contacts_api#test_prospects_search_rejects_unauthenticated_request`

**Error**
```
AssertionError: assert 200 == 401
 +  where 200 = <Response [200 OK]>.status_code
```

<details><summary>Trace</summary>

```
api_client = <clients.api_client.ApiClient object at 0x109d20d90>
credentials = <function get_credentials at 0x109cfb060>

    @pytest.mark.known_bug
    def test_prospects_search_rejects_unauthenticated_request(api_client, credentials):
        """FLAG (security): unlike every other Contacts search endpoint above,
        /pms/prospects/search does not enforce authentication at all when given
        a real property id - a request with no Authorization header returns 200
        with actual prospect PII (name, email, ...), not 401. An invalid/made-up
        property id does correctly 422 first (masking the gap unless you already
        know a real property id), which is what made this easy to miss. Marked
        known_bug per this repo's convention (see pyproject.toml/README): asserts
        the correct expected behavior and is expected to fail until fixed
        upstream, without blocking the main suite."""
        creds = credentials("liberty")
        org_api_base = api_client.resolve_org_api_base(creds["organization_slug"])
    
        response = _search_prospects(api_client, org_api_base, property_id="12613aac-76b8-4d64-a6ca-c388ff1cd438")
    
>       assert response.status_code == 401
E       assert 200 == 401
E        +  where 200 = <Response [200 OK]>.status_code

tests/api/test_contacts_api.py:390: AssertionError
```

</details>

Screenshots/videos/traces for this run are in the `test-results/` or `playwright-artifacts` CI artifact.

---
