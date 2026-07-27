from playwright.sync_api import Page

from pages.base_page import BasePage


class EmployeeDetailPage(BasePage):
    """Employee Detail page, reached by clicking a row on ContactsListPage
    (Employees section).

    DOM scan finding: like VendorDetailPage, this page carries no
    `data-qa-id` of its own outside its three embedded tables (Associated
    Organizations, Associated Properties, Communications Log), which reuse
    the list pages' `table-sort-<field>-btn` / `table-row-<n>` convention.
    On the live Liberty org, Associated Organizations and Communications Log
    always render an empty placeholder row ("- - -") for every employee,
    while Associated Properties had one real row (fields: fullName, address,
    showcaseOrder, balance) - matching VendorDetailPage's field set.
    Crucially, Associated Properties' and Communications Log's row-0 and
    Associated Organizations'/Associated Properties' sort buttons are *not*
    uniquely keyed page-wide - e.g. `[data-qa-id="table-row-0"]` alone
    matches both the real Associated Properties row and Communications
    Log's empty placeholder row, violating Playwright's strict mode - so
    row()/sort_button() below scope to the Associated Properties `mat-card`
    by its title text rather than querying `data-qa-id` directly against
    the page. Activity Log carries no data-qa-id at all.

    This is the only Contacts detail page with two "Edit" buttons on the
    same page (Summary card and Associated Organizations card) - a plain
    `get_by_role("button", name="Edit")` violates Playwright's strict mode,
    so each is scoped to its own `mat-card-title` container (confirmed via
    DOM scan: every card's title text includes its section name plus its
    action button labels, e.g. "Summary Edit", "Associated Organizations
    Edit").

    Also unique to this page: an "Activity Log" section (login/session
    history), not present on any other Contacts detail page.

    API-level finding: the row-click navigates to GET /pms/users/{id} - the
    same detail endpoint HomeownerDetailPage's row-click hits (see
    test_employee_detail_matches_search_result in test_contacts_api.py) -
    even though the search endpoint (/pms/employees/search) is distinct
    from Homeowners' (/pms/users/search).
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.heading = page.get_by_role("heading", name="Employee Details", level=1)
        self.email_employee_button = page.get_by_role("button", name="Email Employee")
        # Not marked up as semantic headings on the live site - plain text.
        self.summary_heading = page.get_by_text("Summary", exact=True)
        self.employee_portal_heading = page.get_by_text("Employee Portal", exact=True)
        self.associated_organizations_heading = page.get_by_text("Associated Organizations", exact=True)
        self.associated_properties_heading = page.get_by_text("Associated Properties", exact=True)
        self.communications_log_heading = page.get_by_text("Communications Log", exact=True)
        self.activity_log_heading = page.get_by_text("Activity Log", exact=True)

        # Two "Edit" buttons on this page - scope each to its own card by title text.
        self.summary_edit_button = page.locator("mat-card-title", has_text="Summary").get_by_role(
            "button", name="Edit"
        )
        self.associated_organizations_edit_button = page.locator(
            "mat-card-title", has_text="Associated Organizations"
        ).get_by_role("button", name="Edit")

        # Employee Portal card - like HomeownerDetailPage, which control is
        # enabled depends on the specific employee's portalStatus.
        self.reset_password_button = page.get_by_role("button", name="Reset Password")
        self.send_password_reset_button = page.get_by_role("button", name="Send Password Reset")
        self.log_in_as_button = page.get_by_role("button", name="Log in as")
        self.activate_portal_button = page.get_by_role("button", name="Activate Portal")
        self.deactivate_portal_button = page.get_by_role("button", name="Deactivate Portal")

        # Communications Log section action buttons - no data-qa-id, role/text fallback.
        self.add_new_button = page.get_by_role("button", name="Add New")
        self.send_email_button = page.get_by_role("button", name="Send Email")
        self.sms_blast_button = page.get_by_role("button", name="SMS Blast")

        # Activity Log section.
        self.view_all_button = page.get_by_role("button", name="View All")

        # Associated Properties card - scoped by title text since its
        # data-qa-id table-row-0/sort buttons collide with Communications
        # Log's own (empty) table (see DOM scan finding above).
        self.associated_properties_card = page.locator("mat-card", has_text="Associated Properties")

    def row(self, index: int):
        """A row in the Associated Properties table (the only one of the
        three embedded tables with data on the live Liberty org) by its
        zero-based position."""
        return self.associated_properties_card.locator(f'[data-qa-id="table-row-{index}"]')

    def sort_button(self, field: str):
        """An Associated Properties column header's sort button, e.g.
        sort_button("fullName")."""
        return self.associated_properties_card.locator(f'[data-qa-id="table-sort-{field}-btn"]')
