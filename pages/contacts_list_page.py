from playwright.sync_api import Page

from pages.base_page import BasePage


class ContactsListPage(BasePage):
    """Generic page object for the Contacts module's seven list pages
    (Customer Accounts, Homeowners, Tenants, Vendors, Developers, Employees,
    Prospects). All seven share the same table/toolbar shape, so one
    parametrized class covers all of them instead of seven near-duplicates
    (see CONTACTS_SECTIONS in tests/e2e/conftest.py for the per-section
    config).

    DOM scan finding: on the live site, `data-qa-id` is only present on the
    table itself (`table-sort-<field>-btn`, `table-select-all-checkbox`,
    `table-row-<n>`, `table-pagination`, `table-empty-state`) - confirmed
    identical across all seven sections. The sidebar nav, quick-filter chips
    and their popovers, the "All Filters" side panel, and the "Create New"
    wizards carry no `data-qa-id` at all, so those fall back to role/text
    locators, matching the rest of this suite (see LeasingActivePage).
    """

    def __init__(self, page: Page, *, menu_item_name: str, heading_text: str):
        super().__init__(page)
        self.menu_item_name = menu_item_name
        self.heading_text = heading_text

        self.contacts_nav_button = page.get_by_role("button", name="Contacts", exact=True)
        self.menu_item = page.get_by_role("menuitem", name=menu_item_name, exact=True)
        self.heading = page.get_by_role("heading", name=heading_text, level=1)

        # Table - the only part of this module instrumented with data-qa-id.
        self.select_all_checkbox = page.locator('[data-qa-id="table-select-all-checkbox"]')
        self.pagination = page.locator('[data-qa-id="table-pagination"]')
        self.empty_state = page.locator('[data-qa-id="table-empty-state"]')

        # Toolbar / filters - no data-qa-id on the live site, role-based fallback.
        # Filter chips are scoped to the `.fb-filter-bar__chips` container:
        # a same-named "Name" role=button also exists on the table's
        # sortable column header (get_by_role("button", name="Name") alone
        # resolves to both and violates Playwright's strict mode).
        self.filter_bar = page.locator(".fb-filter-bar__chips")
        self.all_filters_button = page.get_by_role("button", name="All Filters")
        self.reset_button = page.get_by_role("button", name="Reset", exact=True)
        self.filters_panel_heading = page.get_by_role("heading", name="Filters")
        self.filters_panel_close_button = page.get_by_role("button", name="Close filter panel")
        self.clear_filters_button = page.get_by_role("button", name="Clear Filters")
        self.search_filters_button = page.get_by_role("button", name="Search Filters")
        self.quick_filter_search_button = page.get_by_role("button", name="Search Filter", exact=True)
        self.quick_filter_clear_button = page.get_by_role("button", name="Clear", exact=True)

    def open(self):
        """Navigate to this section via the Contacts sidebar nav. Requires an already signed-in session."""
        self.contacts_nav_button.click()
        self.menu_item.click()
        return self

    def sort_button(self, field: str):
        """A column header's sort button, e.g. sort_button("name")."""
        return self.page.locator(f'[data-qa-id="table-sort-{field}-btn"]')

    def row(self, index: int):
        """A table row by its zero-based position on the current page."""
        return self.page.locator(f'[data-qa-id="table-row-{index}"]')

    def filter_chip(self, name: str):
        return self.filter_bar.get_by_role("button", name=name, exact=True)

    def open_quick_filter(self, chip):
        chip.click()
        return self

    def open_all_filters(self):
        self.all_filters_button.click()
        return self
