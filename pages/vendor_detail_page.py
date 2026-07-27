from playwright.sync_api import Page

from pages.base_page import BasePage


class VendorDetailPage(BasePage):
    """Vendor Detail page, reached by clicking a row on ContactsListPage
    (Vendors section).

    DOM scan finding: like CustomerAccountDetailPage and HomeownerDetailPage,
    this page carries no `data-qa-id` of its own outside its four embedded
    tables (Communication Log, Work Orders, Vendor Staff, Associated
    Properties), which reuse the list pages' `table-sort-<field>-btn` /
    `table-row-<n>` convention. On the live Liberty org only Associated
    Properties had data (fields: fullName, address, showcaseOrder, balance);
    the other three sections rendered "No data available", so tests target
    that one for row/sort assertions.

    API-level finding: the row-click navigates the UI to
    GET /pms/vendors/{groupId}/{propertyId}, not /pms/vendors/{id} like
    Customer Accounts - see test_vendor_detail_matches_search_result in
    test_contacts_api.py for why that response's own `id` differs from the
    search result's `id`.
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.heading = page.get_by_role("heading", name="Vendor Details", level=1)
        self.view_register_button = page.get_by_role("button", name="View Register")
        self.email_vendor_button = page.get_by_role("button", name="Email Vendor")
        self.edit_button = page.get_by_role("button", name="Edit")
        # Not marked up as semantic headings on the live site - plain text.
        self.summary_heading = page.get_by_text("Summary", exact=True)
        self.communication_log_heading = page.get_by_text("Communication Log", exact=True)
        self.work_orders_heading = page.get_by_text("Work Orders", exact=True)
        self.vendor_staff_heading = page.get_by_text("Vendor Staff", exact=True)
        self.associated_properties_heading = page.get_by_text("Associated Properties", exact=True)

        # Section action buttons - no data-qa-id, role/text fallback.
        self.add_work_order_button = page.get_by_role("button", name="Add Work Order")
        self.add_staff_button = page.get_by_role("button", name="Add Staff")
        self.link_property_button = page.get_by_role("button", name="Link Property")

    def row(self, index: int):
        """A row in the Associated Properties table (the only one of the
        four embedded tables with data on the live Liberty org) by its
        zero-based position."""
        return self.page.locator(f'[data-qa-id="table-row-{index}"]')

    def sort_button(self, field: str):
        """An Associated Properties column header's sort button, e.g.
        sort_button("fullName")."""
        return self.page.locator(f'[data-qa-id="table-sort-{field}-btn"]')
