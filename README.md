# hoa-manager-web-tests

Automated test suite for **hoa-manager-web** — a property management
platform used by property managers to run their portfolios. The platform is
multi-tenant: each client is scoped to its own `organization_id`, and the
same deployment serves many organizations. The suite covers both the
frontend (browser, Playwright) and the backend (API, httpx) (Python +
pytest).

## Setup

```bash
uv sync
uv run playwright install chromium
```

`uv` manages its own Python interpreter per `.python-version` /
`requires-python`, so your system Python version doesn't matter.

## Configuration

Copy `.env.example` to `.env` and fill in:

- `PYTEST_BASE_URL` — frontend URL for `tests/e2e` (defaults to `https://roamstay.com`)
- `API_BASE_URL` — backend **directory** API for `tests/api` (defaults to `https://api.roamstay.com`); each organization is then served from its own host (e.g. `https://api.liberty.roamstay.com`), resolved at test time via `ApiClient.resolve_org_api_base()`
- per-organization credentials (see `credentials.py`), including `organization_slug` — the full groupCode the backend expects (e.g. `liberty-community-management-inc`), distinct from `organization_id` which is just the UI search term

`PYTEST_BASE_URL` can also be passed on the command line:

```bash
uv run pytest --base-url=http://localhost:3000
```

## Running tests

```bash
uv run pytest                     # run everything: frontend + backend
uv run pytest -m frontend         # UI/E2E tests only (tests/e2e)
uv run pytest -m backend          # API tests only (tests/api)
uv run pytest -m smoke            # only smoke-tagged tests
uv run pytest --headed            # run with a visible browser
uv run pytest --browser=firefox   # run against Firefox instead of Chromium
```

Failed frontend tests automatically save a screenshot, video, and trace under
`test-results/`. View a trace with:

```bash
uv run playwright show-trace test-results/<test-folder>/trace.zip
```

## Project structure

```
pages/           # Page Object Model classes (one per page/component), used by tests/e2e
clients/         # API client wrappers (httpx), used by tests/api
tests/e2e/       # Frontend/UI test specs (Playwright)
tests/api/       # Backend/API test specs (httpx)
scripts/         # generate_bug_report.py — per-team markdown bug reports
conftest.py      # Shared fixtures + auto-tagging of Allure epic/feature labels
```

Add new pages under `pages/`, wire them up as fixtures in
`tests/e2e/conftest.py`, and write specs under `tests/e2e/`. Add new API
tests the same way under `tests/api/`, using the `api_client` fixture from
`tests/api/conftest.py`.

## Reporting (Allure)

Every test run writes [Allure](https://allurereport.org/) results to
`allure-results/`. Each test is auto-tagged (see `conftest.py`) with:

- **epic** — the test suite/module, e.g. `Sign In`, `Home Page`
- **feature** — the layer, `Frontend` or `Backend`

so the same report can be sliced either by suite or by layer, with zero
per-test decorators needed. View it locally (requires the `allure` CLI —
`brew install allure` or `npm i -g allure-commandline`):

```bash
uv run pytest
allure serve allure-results   # generates + opens the HTML report in one step
```

Or generate the static HTML report and serve it yourself:

```bash
uv run pytest || true
allure generate allure-results --clean -o allure-report
python3 -m http.server 4567 --directory allure-report
```

Then open `http://localhost:4567`. Don't open `allure-report/index.html`
directly via `file://` — the report fetches its data over HTTP and won't
render.

`allure-results/` (raw data) and `allure-report/` (generated HTML) are both
gitignored — they're build output, regenerated every run, never committed.

## Bug reports (per team)

After a run, `scripts/generate_bug_report.py` reads `allure-results/` and
writes one markdown doc per Frontend/Backend + suite combination under
`reports/bug-reports/<feature>/<suite>.md` — e.g. a sign-in bug that only
fails on the backend produces `reports/bug-reports/backend/sign-in.md`,
scoped to just what the backend team needs to act on. Run it manually:

```bash
uv run pytest || true
uv run python scripts/generate_bug_report.py
```

## CI

`.github/workflows/playwright.yml` runs the suite on GitHub Actions:

- on push to `main`
- on pull requests targeting `main`
- nightly at 03:00 UTC (catches drift on the live/staging site)
- manually via the "Run workflow" button (`workflow_dispatch`)

It installs dependencies with `uv`, installs Chromium, runs `pytest`
(frontend + backend), generates per-team bug reports, generates the Allure
HTML report, and uploads as build artifacts: screenshots/videos/traces (on
failure), the bug reports (on failure), and the **Allure HTML report**
(always — this is the report document, generated whether the run passed or
failed).

To view a downloaded `allure-report` artifact: unzip it and serve the
folder (its `index.html` won't work opened directly via `file://` — the
report fetches its data over HTTP). E.g. `python3 -m http.server 4567
--directory allure-report` then open `http://localhost:4567`.

To point CI at different targets than the defaults, set repository/environment
variables (Settings → Secrets and variables → Actions → Variables):
`PYTEST_BASE_URL`, `API_BASE_URL`.
