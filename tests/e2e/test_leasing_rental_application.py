import allure
import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_sign_in_opens_rental_applications(signed_in_rental_applications_page):
    expect(signed_in_rental_applications_page.heading).to_be_visible()
    expect(signed_in_rental_applications_page.table).to_be_visible()


def test_quick_filter_chip_opens_menu(signed_in_rental_applications_page):
    rental_page = signed_in_rental_applications_page

    rental_page.open_quick_filter(rental_page.name_filter_chip)

    expect(rental_page.filter_menu).to_be_visible()


def test_add_rental_application_modal_renders(signed_in_rental_applications_page, add_rental_application_page):
    rental_page = signed_in_rental_applications_page

    rental_page.start_add_application()

    expect(add_rental_application_page.dialog_heading).to_be_visible()
    expect(add_rental_application_page.add_prospect_button).to_be_visible()
    expect(add_rental_application_page.association_select).to_be_visible()
    expect(add_rental_application_page.unit_select).to_be_visible()
    expect(add_rental_application_page.assigned_to_select).to_be_visible()
    expect(add_rental_application_page.desired_move_in_input).to_be_visible()
    expect(add_rental_application_page.specify_fees_toggle).to_be_visible()

    # Exit the modal without saving.
    add_rental_application_page.cancel_button.click()
    expect(add_rental_application_page.dialog_heading).not_to_be_visible()


@pytest.mark.smoke
def test_created_application_appears_correctly_in_list(signed_in_rental_applications_page, seeded_rental_application):
    rental_page = signed_in_rental_applications_page
    application = seeded_rental_application["application"]

    rental_page.all_applications_tab.click()

    # The list defaults to 10 rows/page and this org has accumulated more
    # than that from prior test runs, so a freshly created row can land on
    # page 2+ regardless of sort order. Widen the page size so the new row
    # is guaranteed to be on the (only) page, rather than depending on sort.
    rental_page.page.get_by_role("combobox", name="Items per page:").click()
    rental_page.page.get_by_role("option", name="100", exact=True).click()

    row = rental_page.table.locator("tr", has_text=application["lastName"])
    expect(row).to_be_visible(timeout=10000)
    expect(row).to_contain_text("12/01/2026")
    expect(row).to_contain_text(application["email"])
    # Unit name deliberately not asserted here - see the known-bug test
    # below (test_list_and_detail_agree_on_unit_for_same_application).


@pytest.mark.smoke
def test_created_application_detail_page_shows_correct_values(
    authenticated_page, rental_application_detail_page, seeded_rental_application
):
    application = seeded_rental_application["application"]
    unit_name = seeded_rental_application["unit_name"]
    assigned_user_name = seeded_rental_application["assigned_user_name"]

    # Deep-link straight to the detail page rather than clicking through the
    # list, since the record's list position isn't guaranteed (see
    # test_created_application_appears_correctly_in_list).
    authenticated_page.goto(f"https://liberty.roamstay.com/leasing/rental/{application['id']}")

    detail_page = rental_application_detail_page
    # Generous timeout: this is a cold direct navigation (full app bootstrap),
    # unlike navigating there via in-app clicks.
    expect(detail_page.heading).to_be_visible(timeout=15000)
    # The heading renders before the Overview tab's own data finishes
    # loading (it shows a progressbar briefly), so give the first piece of
    # tab content extra time too.
    expect(detail_page.page.get_by_text("Pending", exact=True).first).to_be_visible(timeout=10000)
    expect(detail_page.page.get_by_text(application["email"], exact=True)).to_be_visible()
    expect(detail_page.page.get_by_role("heading", name=unit_name)).to_be_visible()
    expect(detail_page.page.get_by_text(assigned_user_name, exact=True)).to_be_visible()
    expect(detail_page.page.get_by_text("12/01/2026", exact=True)).to_be_visible()


# --- Known bugs -------------------------------------------------------------
# These assert the *correct* expected behavior rather than the site's current
# (buggy) behavior, so they fail today and will start passing on their own
# once the underlying product bug is fixed - no code changes needed here at
# that point. They're not skipped/xfailed, so they show up as real failures
# in the Allure report and get picked up by scripts/generate_bug_report.py,
# the same way any other regression would. They're marked `known_bug` so CI
# can run them in a separate, non-blocking job (see .github/workflows) -
# tracked and visible without failing the PR check on every run.


@pytest.mark.known_bug
@allure.tag("known-bug")
def test_all_filters_button_opens_panel(signed_in_rental_applications_page):
    """Known bug: "All Filters" does nothing on Rental Applications.

    Verified live: forced clicks, bounding-box target-point checks, and 1.5s
    of DOM polling all show no overlay/heading ever appears. The equivalent
    button on Active Leases works correctly and opens a "Filters" panel
    (see LeasingActivePage.open_all_filters / test_all_filters_panel_opens_and_closes)
    - this asserts Rental Applications should behave the same way.
    """
    rental_page = signed_in_rental_applications_page

    rental_page.open_all_filters()

    expect(rental_page.filters_panel_heading).to_be_visible()


@pytest.mark.known_bug
@allure.tag("known-bug")
def test_list_and_detail_agree_on_unit_for_same_application(
    signed_in_rental_applications_page, seeded_rental_application
):
    """Known bug: the list row and detail page for the same application can
    show different units. Observed for one application: detail page said
    "Lot 14" while the list row for that identical application (matched by
    unique applicant name/email) showed "3738 Reserve Overlook". This
    asserts both views should agree on the unit, using the detail page's
    value (from GET /pms/applications/{id}) as the source of truth.
    """
    rental_page = signed_in_rental_applications_page
    application = seeded_rental_application["application"]
    unit_name = seeded_rental_application["unit_name"]

    rental_page.all_applications_tab.click()
    rental_page.page.get_by_role("combobox", name="Items per page:").click()
    rental_page.page.get_by_role("option", name="100", exact=True).click()

    row = rental_page.table.locator("tr", has_text=application["lastName"])
    expect(row).to_be_visible(timeout=10000)
    expect(row).to_contain_text(unit_name)
