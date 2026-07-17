from playwright.sync_api import Page

from pages.base_page import BasePage


class LeasingActivePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.leasing_nav_button = page.get_by_role("button", name="Leasing")
        self.active_leases_menu_item = page.get_by_role("menuitem", name="Active Leases")
        self.heading = page.get_by_role("heading", name="Active Leases", level=1)
        self.pending_tab = page.get_by_role("button", name="Pending")
        self.all_active_leases_tab = page.get_by_role("button", name="All Active Leases")
        self.table = page.locator("table").first
        self.empty_state = page.get_by_text("Nothing to display")

        # Quick filter chips (toolbar)
        self.name_filter_chip = page.get_by_role("button", name="Name", exact=True)
        self.association_filter_chip = page.get_by_role("button", name="Association", exact=True)
        self.term_filter_chip = page.get_by_role("button", name="Term", exact=True)
        self.rent_filter_chip = page.get_by_role("button", name="Rent", exact=True)
        self.deposit_filter_chip = page.get_by_role("button", name="Deposit", exact=True)
        self.balance_filter_chip = page.get_by_role("button", name="Balance", exact=True)
        self.all_filters_button = page.get_by_role("button", name="All Filters")
        self.reset_button = page.get_by_role("button", name="Reset")

        # Quick filter chip popover (shared shape: one field + Clear + Search Filter)
        self.quick_filter_search_button = page.get_by_role("button", name="Search Filter", exact=True)
        self.quick_filter_clear_button = page.get_by_role("button", name="Clear", exact=True)

        # "All Filters" side panel
        self.filters_panel_heading = page.get_by_role("heading", name="Filters")
        self.filters_panel_close_button = page.get_by_role("button", name="Close filter panel")
        self.filter_name_input = page.get_by_placeholder("Name", exact=True)
        self.filter_association_input = page.get_by_placeholder("Association", exact=True)
        self.filter_term_input = page.get_by_placeholder("Term", exact=True)
        self.clear_filters_button = page.get_by_role("button", name="Clear Filters")
        self.search_filters_button = page.get_by_role("button", name="Search Filters")

        # Add Lease entry point (two duplicate nodes exist for responsive layouts)
        self.add_lease_quick_action = page.get_by_text("Add Lease", exact=False).first

    def open(self):
        """Navigate to Active Leases via the Leasing sidebar nav. Requires an already signed-in session."""
        self.leasing_nav_button.click()
        self.active_leases_menu_item.click()
        return self

    def open_quick_filter(self, chip):
        chip.click()
        return self

    def open_all_filters(self):
        self.all_filters_button.click()
        return self

    def start_add_lease(self):
        """Open the Add Lease wizard's welcome screen."""
        self.add_lease_quick_action.click()
        return self
