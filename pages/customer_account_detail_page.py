from playwright.sync_api import Page

from pages.base_page import BasePage


class CustomerAccountDetailPage(BasePage):
    """Customer Account Details page, reached by clicking a row on
    ContactsListPage (Customer Accounts section).

    DOM scan finding: this page carries no `data-qa-id` at all - not even on
    the Summary card or the Edit/View Register actions. Only the embedded
    message-thread table further down the page reuses the list pages'
    `table-sort-<field>-btn` convention, so this page object is entirely
    role/text based.
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.heading = page.get_by_role("heading", name="Customer Account Details", level=1)
        self.view_register_button = page.get_by_role("button", name="View Register")
        self.edit_button = page.get_by_role("link", name="Edit")
        # Not marked up as a semantic heading on the live site - plain text.
        self.summary_heading = page.get_by_text("Summary", exact=True)
        self.unpaid_charges_card = page.get_by_text("Unpaid Charges")
        self.unapplied_credits_card = page.get_by_text("Unapplied Credits")
        self.total_balance_card = page.get_by_text("Total Balance", exact=True)
