import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_sign_in_opens_active_leases(signed_in_active_leases_page):
    expect(signed_in_active_leases_page.heading).to_be_visible()
    expect(signed_in_active_leases_page.table).to_be_visible()


def test_all_filters_panel_opens_and_closes(signed_in_active_leases_page):
    leasing_page = signed_in_active_leases_page

    leasing_page.open_all_filters()

    expect(leasing_page.filters_panel_heading).to_be_visible()
    expect(leasing_page.filter_name_input).to_be_visible()
    expect(leasing_page.filter_association_input).to_be_visible()
    expect(leasing_page.filter_term_input).to_be_visible()
    expect(leasing_page.clear_filters_button).to_be_visible()
    expect(leasing_page.search_filters_button).to_be_visible()

    leasing_page.filters_panel_close_button.click()
    expect(leasing_page.filters_panel_heading).not_to_be_visible()


def test_quick_filter_chip_opens_popover(signed_in_active_leases_page):
    leasing_page = signed_in_active_leases_page

    leasing_page.open_quick_filter(leasing_page.association_filter_chip)

    expect(leasing_page.quick_filter_search_button).to_be_visible()
    expect(leasing_page.quick_filter_clear_button).to_be_visible()


def test_add_lease_wizard_step_one_renders(signed_in_active_leases_page, add_lease_page):
    leasing_page = signed_in_active_leases_page

    leasing_page.start_add_lease()
    expect(add_lease_page.welcome_heading).to_be_visible()

    add_lease_page.get_started_button.click()
    expect(add_lease_page.step_heading).to_be_visible()
    expect(add_lease_page.association_select).to_be_visible()
    expect(add_lease_page.unit_select).to_be_visible()
    expect(add_lease_page.fixed_term_label).to_be_visible()
    expect(add_lease_page.month_to_month_label).to_be_visible()
    expect(add_lease_page.start_date_input).to_be_visible()
    expect(add_lease_page.add_tenant_button).to_be_visible()
    expect(add_lease_page.next_button).to_be_visible()

    # Verify the "Select Tenant" sub-dialog opens, without creating any data.
    add_lease_page.add_tenant_button.click()
    expect(add_lease_page.select_tenant_heading).to_be_visible()
    expect(add_lease_page.select_tenant_search_input).to_be_visible()
    expect(add_lease_page.select_tenant_add_tenant_link).to_be_visible()
    add_lease_page.select_tenant_cancel_button.click()
    expect(add_lease_page.select_tenant_heading).not_to_be_visible()

    # Exit the wizard without saving.
    add_lease_page.cancel_wizard_link.click()
