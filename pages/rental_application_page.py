from playwright.sync_api import Page

from pages.base_page import BasePage


class RentalApplicationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.leasing_nav_button = page.get_by_role("button", name="Leasing")
        self.rental_applications_menu_item = page.get_by_role("menuitem", name="Rental Applications")
        self.heading = page.get_by_role("heading", name="Rental Applications", level=1)
        self.undecided_tab = page.get_by_role("button", name="Undecided")
        self.all_applications_tab = page.get_by_role("button", name="All Applications")
        self.table = page.locator("table").first
        self.empty_state = page.get_by_text("Nothing to display")

        # Quick filter chips (toolbar), scoped to the filter group since the
        # table's sortable "Name" column header also has role=button name="Name".
        filter_group = page.locator("app-rental-application-filter-group")
        self.name_filter_chip = filter_group.get_by_role("button", name="Name", exact=True)
        self.status_filter_chip = filter_group.get_by_role("button", name="Status", exact=True)
        self.units_filter_chip = filter_group.get_by_role("button", name="Units", exact=True)
        self.move_in_date_filter_chip = filter_group.get_by_role("button", name="Move In Date", exact=True)
        self.contact_filter_chip = filter_group.get_by_role("button", name="Contact", exact=True)
        self.reset_button = page.get_by_role("button", name="Reset")
        # "All Filters" is present but does not open any panel - a live
        # product bug, tracked by test_all_filters_button_opens_panel below
        # (asserts the correct behavior, matching Active Leases' working
        # equivalent, so it currently fails and will pass once fixed).
        self.all_filters_button = page.get_by_role("button", name="All Filters")
        self.filters_panel_heading = page.get_by_role("heading", name="Filters")

        # Quick filter chips open a real Angular Material mat-menu here
        # (role="menu"), unlike Active Leases' custom filter-panel popover -
        # confirmed live; it does not reliably close on Escape.
        self.filter_menu = page.get_by_role("menu")

        # Add Application entry point (two duplicate nodes may exist for
        # responsive layouts, matching the Add Lease quick action's shape).
        self.add_application_quick_action = page.get_by_text("Add Application", exact=False).first

    def open(self):
        """Navigate to Rental Applications via the Leasing sidebar nav. Requires an already signed-in session."""
        self.leasing_nav_button.click()
        self.rental_applications_menu_item.click()
        return self

    def open_quick_filter(self, chip):
        chip.click()
        return self

    def open_all_filters(self):
        self.all_filters_button.click()
        return self

    def start_add_application(self):
        """Open the 'Add Rental Application' modal."""
        self.add_application_quick_action.click()
        return self

    def open_application_row(self, applicant_last_name: str):
        """Click a list row to open its detail page, matched by the
        applicant's last name (expected to be unique per test)."""
        self.page.get_by_text(applicant_last_name, exact=False).first.click()
        return self
