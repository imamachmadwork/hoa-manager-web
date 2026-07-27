import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_contacts_section_list_renders(signed_in_contacts_page):
    """Scans every Contacts sidebar section (Customer Accounts, Homeowners,
    Tenants, Vendors, Developers, Employees, Prospects): the heading renders
    and the table shows either data or the empty state - never a blank/broken
    page. Tenants was observed empty (0 records) on the live Liberty org, so
    both outcomes are treated as valid rather than asserting row count."""
    contacts_page = signed_in_contacts_page

    expect(contacts_page.heading).to_be_visible()
    expect(contacts_page.row(0).or_(contacts_page.empty_state)).to_be_visible()


def test_all_filters_panel_opens_and_closes(signed_in_customer_accounts_page):
    contacts_page = signed_in_customer_accounts_page

    contacts_page.open_all_filters()

    expect(contacts_page.filters_panel_heading).to_be_visible()
    expect(contacts_page.clear_filters_button).to_be_visible()
    expect(contacts_page.search_filters_button).to_be_visible()

    contacts_page.filters_panel_close_button.click()
    expect(contacts_page.filters_panel_heading).not_to_be_visible()


def test_quick_filter_chip_opens_popover(signed_in_customer_accounts_page):
    contacts_page = signed_in_customer_accounts_page

    contacts_page.open_quick_filter(contacts_page.filter_chip("Name"))

    expect(contacts_page.quick_filter_search_button).to_be_visible()
    expect(contacts_page.quick_filter_clear_button).to_be_visible()


def test_sort_column_header_reorders_without_error(signed_in_customer_accounts_page):
    """Clicking a sortable column header re-issues the search (POST
    /pms/customer-accounts/search with a different `sort`/`order`) rather
    than erroring - see test_contacts_api.py for the request/response shape."""
    contacts_page = signed_in_customer_accounts_page

    contacts_page.sort_button("name").click()

    expect(contacts_page.row(0)).to_be_visible()


def test_row_click_opens_customer_account_details(signed_in_customer_accounts_page, customer_account_detail_page):
    contacts_page = signed_in_customer_accounts_page

    contacts_page.row(0).click()

    expect(customer_account_detail_page.heading).to_be_visible()
    expect(customer_account_detail_page.summary_heading).to_be_visible()
    expect(customer_account_detail_page.total_balance_card).to_be_visible()
