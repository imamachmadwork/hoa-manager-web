from playwright.sync_api import Page

from pages.base_page import BasePage


class DeveloperDetailPage(BasePage):
    """Developer Detail page, reached by clicking a row on ContactsListPage
    (Developers section).

    DOM scan finding: unlike CustomerAccountDetailPage/HomeownerDetailPage/
    VendorDetailPage, this page has no "Summary" text at all - the name/status
    card has no heading of its own, just the name, an Active/Inactive pill,
    and Email/Phone Number/Address fields directly. It also has no Edit or
    "Email Developer" action - Link Property, Manage Staff and Add Staff are
    the only buttons on the page (plus Communication Log's Add New/Send
    Email/SMS Blast, not modeled here, matching how VendorDetailPage skips
    that section's actions too).

    On the live Liberty org, every one of its 105 developers has
    countProperties == 0 (Associated Properties always renders "No connected
    properties.") and Developer Staff/Communication Log both render "No data
    available" regardless of the search result's countUsers - so this page
    object doesn't expose row()/sort() helpers for those tables (nothing to
    click), just the section headings and action buttons for presence
    assertions.

    API-level finding: the row-click navigates to GET /pms/groups/{id},
    which wraps the record in a single-element `group` array (`{"group":
    [{...}]}`) rather than returning it directly - see
    test_developer_detail_matches_search_result in test_contacts_api.py.
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.heading = page.get_by_role("heading", name="Developer Details", level=1)
        self.link_property_button = page.get_by_role("button", name="Link Property")
        # Not marked up as semantic headings on the live site - plain text.
        self.associated_properties_heading = page.get_by_text("Associated Properties", exact=True)
        self.developer_staff_heading = page.get_by_text("Developer Staff", exact=True)
        self.communication_log_heading = page.get_by_text("Communication Log", exact=True)

        # Developer Staff section action buttons - no data-qa-id, role/text fallback.
        self.manage_staff_button = page.get_by_role("button", name="Manage Staff")
        self.add_staff_button = page.get_by_role("button", name="Add Staff")
