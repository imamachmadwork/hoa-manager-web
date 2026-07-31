# Leasing Rental Application Api — Backend bugs

- Generated: 2026-07-31 09:00 UTC
- Environment: https://roamstay.com
- Failing tests: 1

## test_created_application_appears_in_search

- Status: `failed`
- Full name: `tests.api.test_leasing_rental_application_api#test_created_application_appears_in_search`

**Error**
```
AssertionError: assert '7802ea1e-772f-4eea-baa6-308843d91ea6' in ['d0871d39-05cf-472a-b307-04c6eb2c1fee', 'f8772bf2-1e6d-4c15-80fe-027aabeb2788', 'a0ac7684-ff58-4bb6-841e-ba742a0eeb2c...e149-f611-4dd4-9528-d8bbbd5d90a9', 'ae9d6b22-9da0-4f75-9ae0-7fb09bb7a5f9', '74321b1b-11ff-4981-8184-50f4e4d5d653', ...]
```

<details><summary>Trace</summary>

```
api_client = <clients.api_client.ApiClient object at 0x10787d810>
authenticated_session = {'org_api_base': 'https://api.liberty.roamstay.com'}
default_property_id = '12613aac-76b8-4d64-a6ca-c388ff1cd438'
created_application = {'propertyId': '12613aac-76b8-4d64-a6ca-c388ff1cd438', 'userId': '178be1e9-5649-4e84-b31f-b25fa7ad33d5', 'unitId': '559a75a8-2ba7-41d7-b60d-aece49af4295', 'assignedUserId': '1954dea7-2fbf-492d-82e5-a74e2118cc3e', ...}

    @pytest.mark.smoke
    def test_created_application_appears_in_search(
        api_client, authenticated_session, default_property_id, created_application
    ):
        # This org has accumulated many applications from repeated test runs, so
        # a small page size (matching the UI's default of 10) isn't guaranteed
        # to include a freshly created record - widen it for this assertion.
        response = _search_applications(
            api_client, authenticated_session["org_api_base"], default_property_id, [], limit=100
        )
    
        assert response.status_code == 200
        ids = [row["id"] for row in response.json()["data"]]
>       assert created_application["id"] in ids
E       AssertionError: assert '7802ea1e-772f-4eea-baa6-308843d91ea6' in ['d0871d39-05cf-472a-b307-04c6eb2c1fee', 'f8772bf2-1e6d-4c15-80fe-027aabeb2788', 'a0ac7684-ff58-4bb6-841e-ba742a0eeb2c...e149-f611-4dd4-9528-d8bbbd5d90a9', 'ae9d6b22-9da0-4f75-9ae0-7fb09bb7a5f9', '74321b1b-11ff-4981-8184-50f4e4d5d653', ...]

tests/api/test_leasing_rental_application_api.py:132: AssertionError
```

</details>

Screenshots/videos/traces for this run are in the `test-results/` or `playwright-artifacts` CI artifact.

---
