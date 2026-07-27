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


def test_homeowners_all_filters_panel_opens_and_closes(signed_in_homeowners_page):
    contacts_page = signed_in_homeowners_page

    contacts_page.open_all_filters()

    expect(contacts_page.filters_panel_heading).to_be_visible()
    expect(contacts_page.clear_filters_button).to_be_visible()
    expect(contacts_page.search_filters_button).to_be_visible()

    contacts_page.filters_panel_close_button.click()
    expect(contacts_page.filters_panel_heading).not_to_be_visible()


def test_homeowners_quick_filter_chip_opens_popover(signed_in_homeowners_page):
    contacts_page = signed_in_homeowners_page

    contacts_page.open_quick_filter(contacts_page.filter_chip("Name"))

    expect(contacts_page.quick_filter_search_button).to_be_visible()
    expect(contacts_page.quick_filter_clear_button).to_be_visible()


def test_homeowners_sort_column_header_reorders_without_error(signed_in_homeowners_page):
    """Clicking a sortable column header re-issues the search (POST
    /pms/users/search with a different `sort`/`order`) rather than erroring -
    see test_contacts_api.py for the request/response shape."""
    contacts_page = signed_in_homeowners_page

    contacts_page.sort_button("name").click()

    expect(contacts_page.row(0)).to_be_visible()


def test_row_click_opens_homeowner_details(signed_in_homeowners_page, homeowner_detail_page):
    contacts_page = signed_in_homeowners_page

    contacts_page.row(0).click()

    expect(homeowner_detail_page.heading).to_be_visible()
    expect(homeowner_detail_page.summary_heading).to_be_visible()
    expect(homeowner_detail_page.email_homeowner_button).to_be_visible()
    expect(homeowner_detail_page.edit_button).to_be_visible()
    expect(homeowner_detail_page.unit_owned_heading).to_be_visible()


def test_vendors_all_filters_panel_opens_and_closes(signed_in_vendors_page):
    contacts_page = signed_in_vendors_page

    contacts_page.open_all_filters()

    expect(contacts_page.filters_panel_heading).to_be_visible()
    expect(contacts_page.clear_filters_button).to_be_visible()
    expect(contacts_page.search_filters_button).to_be_visible()

    contacts_page.filters_panel_close_button.click()
    expect(contacts_page.filters_panel_heading).not_to_be_visible()


def test_vendors_quick_filter_chip_opens_popover(signed_in_vendors_page):
    contacts_page = signed_in_vendors_page

    contacts_page.open_quick_filter(contacts_page.filter_chip("Name"))

    expect(contacts_page.quick_filter_search_button).to_be_visible()
    expect(contacts_page.quick_filter_clear_button).to_be_visible()


def test_vendors_sort_column_header_reorders_without_error(signed_in_vendors_page):
    """Clicking a sortable column header re-issues the search (POST
    /pms/vendors/search with a different `sort`/`order`) rather than
    erroring - see test_contacts_api.py for the request/response shape."""
    contacts_page = signed_in_vendors_page

    contacts_page.sort_button("name").click()

    expect(contacts_page.row(0)).to_be_visible()


def test_row_click_opens_vendor_details(signed_in_vendors_page, vendor_detail_page):
    """Vendor Details has four embedded tables (Communication Log, Work
    Orders, Vendor Staff, Associated Properties) alongside the Summary card
    - see VendorDetailPage for the DOM scan behind these locators."""
    contacts_page = signed_in_vendors_page

    contacts_page.row(0).click()

    expect(vendor_detail_page.heading).to_be_visible()
    expect(vendor_detail_page.summary_heading).to_be_visible()
    expect(vendor_detail_page.view_register_button).to_be_visible()
    expect(vendor_detail_page.email_vendor_button).to_be_visible()
    expect(vendor_detail_page.edit_button).to_be_visible()
    expect(vendor_detail_page.associated_properties_heading).to_be_visible()


def test_developers_all_filters_panel_opens_and_closes(signed_in_developers_page):
    contacts_page = signed_in_developers_page

    contacts_page.open_all_filters()

    expect(contacts_page.filters_panel_heading).to_be_visible()
    expect(contacts_page.clear_filters_button).to_be_visible()
    expect(contacts_page.search_filters_button).to_be_visible()

    contacts_page.filters_panel_close_button.click()
    expect(contacts_page.filters_panel_heading).not_to_be_visible()


def test_developers_quick_filter_chip_opens_popover(signed_in_developers_page):
    contacts_page = signed_in_developers_page

    contacts_page.open_quick_filter(contacts_page.filter_chip("Name"))

    expect(contacts_page.quick_filter_search_button).to_be_visible()
    expect(contacts_page.quick_filter_clear_button).to_be_visible()


def test_developers_sort_column_header_reorders_without_error(signed_in_developers_page):
    """Clicking a sortable column header re-issues the search (POST
    /pms/groups/search with a different `sort`/`order`) rather than
    erroring - see test_contacts_api.py for the request/response shape."""
    contacts_page = signed_in_developers_page

    contacts_page.sort_button("name").click()

    expect(contacts_page.row(0)).to_be_visible()


def test_row_click_opens_developer_details(signed_in_developers_page, developer_detail_page):
    """Developer Details has no Summary heading or Edit/Email action (unlike
    Customer Accounts/Homeowners/Vendors) - just the name/status card plus
    Associated Properties and Developer Staff, both empty for every developer
    on the live Liberty org. See DeveloperDetailPage for the DOM scan behind
    these locators."""
    contacts_page = signed_in_developers_page

    contacts_page.row(0).click()

    expect(developer_detail_page.heading).to_be_visible()
    expect(developer_detail_page.associated_properties_heading).to_be_visible()
    expect(developer_detail_page.link_property_button).to_be_visible()
    expect(developer_detail_page.developer_staff_heading).to_be_visible()
    expect(developer_detail_page.manage_staff_button).to_be_visible()
    expect(developer_detail_page.add_staff_button).to_be_visible()


def test_employees_all_filters_panel_opens_and_closes(signed_in_employees_page):
    contacts_page = signed_in_employees_page

    contacts_page.open_all_filters()

    expect(contacts_page.filters_panel_heading).to_be_visible()
    expect(contacts_page.clear_filters_button).to_be_visible()
    expect(contacts_page.search_filters_button).to_be_visible()

    contacts_page.filters_panel_close_button.click()
    expect(contacts_page.filters_panel_heading).not_to_be_visible()


def test_employees_quick_filter_chip_opens_popover(signed_in_employees_page):
    contacts_page = signed_in_employees_page

    contacts_page.open_quick_filter(contacts_page.filter_chip("Name"))

    expect(contacts_page.quick_filter_search_button).to_be_visible()
    expect(contacts_page.quick_filter_clear_button).to_be_visible()


def test_employees_sort_column_header_reorders_without_error(signed_in_employees_page):
    """Clicking a sortable column header re-issues the search (POST
    /pms/employees/search with a different `sort`/`order`) rather than
    erroring - see test_contacts_api.py for the request/response shape."""
    contacts_page = signed_in_employees_page

    contacts_page.sort_button("name").click()

    expect(contacts_page.row(0)).to_be_visible()


def test_row_click_opens_employee_details(signed_in_employees_page, employee_detail_page):
    """Employee Details has Summary/Edit and an Employee Portal card (like
    HomeownerDetailPage), plus two Contacts-module-only additions: an
    Associated Organizations table (in addition to Associated Properties)
    and an Activity Log section. See EmployeeDetailPage for the DOM scan
    behind these locators, including how its two "Edit" buttons are
    disambiguated."""
    contacts_page = signed_in_employees_page

    contacts_page.row(0).click()

    expect(employee_detail_page.heading).to_be_visible()
    expect(employee_detail_page.summary_heading).to_be_visible()
    expect(employee_detail_page.email_employee_button).to_be_visible()
    expect(employee_detail_page.summary_edit_button).to_be_visible()
    expect(employee_detail_page.employee_portal_heading).to_be_visible()
    expect(employee_detail_page.reset_password_button).to_be_visible()
    expect(employee_detail_page.send_password_reset_button).to_be_visible()
    expect(employee_detail_page.associated_organizations_heading).to_be_visible()
    expect(employee_detail_page.associated_organizations_edit_button).to_be_visible()
    expect(employee_detail_page.associated_properties_heading).to_be_visible()
    expect(employee_detail_page.communications_log_heading).to_be_visible()
    expect(employee_detail_page.activity_log_heading).to_be_visible()
