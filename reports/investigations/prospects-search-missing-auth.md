# Contacts > Prospects: `/pms/prospects/search` returns real data with no Authorization header

- Investigated: 2026-07-27
- Environment: https://api.liberty.roamstay.com (Liberty org)
- Failing test: `tests/api/test_contacts_api.py::test_prospects_search_rejects_unauthenticated_request`
  (marked `known_bug` - asserts the correct 401, currently gets 200, does not
  block the main CI job)
- Severity: **Security - unauthenticated data exposure**

## Summary

Every other Contacts search endpoint (`customer-accounts/search`,
`users/search`, `vendors/search`) correctly returns `401` when called with no
`Authorization` header. `/pms/prospects/search` does not: given a real
`property` id, it returns `200` with a full page of live prospect records -
name, email, pagination metadata - to a completely anonymous caller.

The gap is easy to miss in casual testing because an *invalid* `property` id
(e.g. a made-up UUID) correctly 422s first, on request validation, before
auth would even be checked. You only see the real behavior if you already
know a valid property id to pass in. That's a low bar for anyone probing this
endpoint from outside - property ids aren't secret (they're visible in URLs
and other API responses throughout the app), so this is exploitable by
anyone who has ever loaded a page in this org, signed in or not.

## Evidence

Request with **no `Authorization` header at all**, real property id:

```
POST https://api.liberty.roamstay.com/pms/prospects/search
{"sortDirection":"desc","sortActive":"date","limit":3,"page":1,
 "property":"12613aac-76b8-4d64-a6ca-c388ff1cd438","filters":{}}

-> 200 OK
{"meta":{"total":57,"per_page":3,"current_page":1,"last_page":19,...},
 "data":[
   {"id":"a36b6b9c-...","name":"QA API","email":"qa.api.rental+...@example.com","contactPhone":null},
   {"id":"86838fe3-...","name":"QA API","email":"qa.api.rental+...@example.com","contactPhone":null},
   ...
 ]}
```

Same request with a **bogus** property id (what you'd try first, without
already knowing a real one) - this is what masks the bug:

```
POST /pms/prospects/search {"...","property":"not-a-real-uuid","filters":{}}
-> 422 {"errors":[{"rule":"uuid","field":"property","message":"uuid validation failed"}, ...]}
```

For comparison, every sibling endpoint rejects the same no-auth request
before it ever gets to validating `property`:

```
POST /pms/customer-accounts/search (no auth) -> 401
POST /pms/users/search             (no auth) -> 401
POST /pms/vendors/search           (no auth) -> 401
POST /pms/prospects/search         (no auth) -> 200  <- the outlier
```

Automated coverage: `tests/api/test_contacts_api.py::test_prospects_search_rejects_unauthenticated_request`
reproduces this deterministically (asserts the correct `401`, currently fails
with `assert 200 == 401`) - see `reports/bug-reports/backend/contacts-api.md`
for the raw failure from the latest run.

## Root cause

Auth middleware appears to be applied per-route (or per-controller) rather
than globally to all `/pms/*` write/search endpoints, and the route/controller
backing `/pms/prospects/search` is missing it - the other three sibling
search endpoints in the same module (Customer Accounts, Users, Vendors) all
have it. This looks like an endpoint that was added without copying the auth
guard from its neighbors, rather than a deliberate "public prospect search"
design (prospects are pre-authentication leads/applicants, but the search
result here includes internal record ids and full contact details, not just
what a public-facing form would need).

## Suggested fix

- Add the same authentication guard used by `customer-accounts/search`,
  `users/search`, and `vendors/search` to the `prospects/search` route/
  controller so it 401s on a missing/invalid session, consistent with every
  other Contacts search endpoint.
- Once fixed, also double check `/pms/prospects` (the create endpoint used by
  the public "Sign Up"/apply flow) isn't accidentally over-restricted by the
  same change - that one *is* expected to work pre-authentication.
- Consider a quick audit of any other `/pms/*` search or list endpoints for
  the same per-route-guard gap, since this was only found because the
  Contacts module test suite happened to check every sibling endpoint - the
  same class of bug could exist elsewhere (Leasing, Maintenance, etc.) and
  wouldn't be caught unless each endpoint is tested individually the way this
  suite does.

## How to reproduce manually

1. Get any valid `property` id for the org (visible in the URL/network tab
   after signing in normally, e.g. via Associations).
2. Send a `POST` to `https://api.<org>.roamstay.com/pms/prospects/search`
   with that `property` id and **no `Authorization` header**, body:
   `{"sortDirection":"desc","sortActive":"date","limit":10,"page":1,"property":"<id>","filters":{}}`.
3. Observe `200 OK` with real prospect names/emails, instead of the `401`
   every other Contacts search endpoint returns for the same kind of request.

## Test status (no action needed until the fix lands)

`test_prospects_search_rejects_unauthenticated_request` is already in the
suite, marked `@pytest.mark.known_bug` per this repo's convention (see
README) - it asserts the correct expected behavior (`401`) and is expected to
keep failing, on its own CI job, until this is fixed upstream. Once the
backend adds the auth guard, the test should pass as-is with no changes
needed.
