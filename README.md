# hoa-manager-web-tests

Playwright end-to-end test suite for **hoa-manager-web** — a property
management platform used by property managers to run their portfolios.
The platform is multi-tenant: each client is scoped to its own
`organization_id`, and the same deployment serves many organizations. The
suite targets the live app at `https://roamstay.com` by default (Python +
pytest).

## Setup

```bash
uv sync
uv run playwright install chromium
```

`uv` manages its own Python interpreter per `.python-version` /
`requires-python`, so your system Python version doesn't matter.

## Configuration

Default target is `https://roamstay.com` (set in `pyproject.toml`). To point at a
different environment, copy `.env.example` to `.env` and set `PYTEST_BASE_URL`,
or pass it on the command line:

```bash
uv run pytest --base-url=http://localhost:3000
```

## Running tests

```bash
uv run pytest                     # run all tests, headless
uv run pytest -m smoke            # run only smoke tests
uv run pytest --headed            # run with a visible browser
uv run pytest --browser=firefox   # run against Firefox instead of Chromium
```

Failed tests automatically save a screenshot, video, and trace under
`test-results/`. View a trace with:

```bash
uv run playwright show-trace test-results/<test-folder>/trace.zip
```

## Project structure

```
pages/    # Page Object Model classes (one per page/component)
tests/    # Test specs
conftest.py  # Shared fixtures (env loading, page object fixtures)
```

Add new pages under `pages/`, wire them up as fixtures in `conftest.py`, and
write specs under `tests/`.

## CI

`.github/workflows/playwright.yml` runs the suite on GitHub Actions:

- on push to `main`
- on pull requests targeting `main`
- nightly at 03:00 UTC (catches drift on the live/staging site)
- manually via the "Run workflow" button (`workflow_dispatch`)

It installs dependencies with `uv`, installs Chromium, runs `pytest`, and
uploads screenshots/videos/traces as a build artifact if a test fails.

To point CI at a different URL than the `https://roamstay.com` default,
set a repository/environment variable named `PYTEST_BASE_URL`
(Settings → Secrets and variables → Actions → Variables).
