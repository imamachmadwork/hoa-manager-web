from playwright.sync_api import Page

from pages.base_page import BasePage


class HomeownerDetailPage(BasePage):
    """Homeowner Detail page, reached by clicking a row on ContactsListPage
    (Homeowners section).

    DOM scan finding: like CustomerAccountDetailPage, this page carries no
    `data-qa-id` of its own - not on Summary, the contact fields, or the
    Homeowner Portal actions. The only exception is the embedded "Unit
    Owned" table further down the page, which reuses the list pages'
    `table-sort-<field>-btn` / `table-row-<n>` convention (fields: name,
    address, unitType.name). Everything else below is role/text based.

    The Homeowner Portal actions (Reset Password, Send Password Reset, Log
    in as) are disabled until the portal is activated - which one is
    enabled depends on the specific homeowner's portalStatus, so tests
    should assert these controls are present rather than assume a
    particular enabled/disabled state.
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.heading = page.get_by_role("heading", name="Homeowner Detail", level=1)
        self.email_homeowner_button = page.get_by_role("button", name="Email Homeowner")
        self.edit_button = page.get_by_role("button", name="Edit")
        # Not marked up as a semantic heading on the live site - plain text.
        self.summary_heading = page.get_by_text("Summary", exact=True)
        self.unit_owned_heading = page.get_by_text("Unit Owned", exact=True)

        # Homeowner Portal card.
        self.reset_password_button = page.get_by_role("button", name="Reset Password")
        self.send_password_reset_button = page.get_by_role("button", name="Send Password Reset")
        self.log_in_as_button = page.get_by_role("button", name="Log in as")
        self.activate_portal_button = page.get_by_role("button", name="Activate Portal")

        # Unit Owned table - the only part of this page instrumented with data-qa-id.
        self.unit_empty_state = page.get_by_text("No data available")

    def unit_row(self, index: int):
        """A row in the Unit Owned table by its zero-based position."""
        return self.page.locator(f'[data-qa-id="table-row-{index}"]')

    def unit_sort_button(self, field: str):
        """A Unit Owned column header's sort button, e.g. unit_sort_button("name")."""
        return self.page.locator(f'[data-qa-id="table-sort-{field}-btn"]')
