from playwright.sync_api import Page

from pages.base_page import BasePage


class AddLeasePage(BasePage):
    """The 'Add Lease' wizard, reached from LeasingActivePage.start_add_lease().

    Only covers the welcome screen and step 1 ("Get Started"), plus the
    Select Tenant sub-dialog it opens. Steps 2-3 (disclosures, e-signature)
    require a tenant to already exist and are not covered here.
    """

    def __init__(self, page: Page):
        super().__init__(page)
        # Welcome screen
        self.welcome_heading = page.get_by_text("It’s easy to add a lease on Roam")
        self.get_started_button = page.get_by_role("button", name="Get Started")
        self.dont_show_again_checkbox = page.get_by_text("Don't show this welcome screen again")

        # Step 1 ("Get Started") form
        self.step_heading = page.get_by_role("heading", name="Get Started")
        self.association_select = page.locator("app-roam-select[formcontrolname='property']")
        self.unit_select = page.locator("app-roam-select[formcontrolname='unit']")
        # The native radio inputs are visually hidden behind styled labels;
        # use `.check(force=True)` to select them, get_by_text(...) to assert visibility.
        self.fixed_term_radio = page.locator("input[type='radio'][value='Fixed Term']")
        self.month_to_month_radio = page.locator("input[type='radio'][value='Month-to month']")
        self.fixed_term_label = page.get_by_text("Fixed Term", exact=True)
        self.month_to_month_label = page.get_by_text("Month-to month", exact=True)
        self.start_date_input = page.get_by_label("Start Date")
        self.rollover_toggle = page.get_by_text("Rollover to “Month to Month” at the end of the term")
        self.add_tenant_button = page.get_by_role("button", name="Add Tenant")
        self.next_button = page.get_by_role("button", name="Next")
        self.save_and_exit_button = page.get_by_role("button", name="Save & Exit")
        # Scoped to the step footer, since "Cancel" also appears inside the
        # Select Tenant sub-dialog when it's open.
        self.cancel_wizard_link = page.locator("#stepper-pagination").get_by_text("Cancel", exact=True)

        # "Select Tenant" sub-dialog (opened via add_tenant_button)
        self.select_tenant_heading = page.get_by_role("heading", name="Select Tenant")
        self.select_tenant_search_input = page.get_by_placeholder("Search", exact=True)
        self.select_tenant_add_tenant_link = page.locator("button-underline").get_by_text("Add Tenant", exact=True)
        self.select_tenant_cancel_button = page.get_by_role("button", name="Cancel", exact=True)
        self.select_tenant_select_button = page.get_by_role("button", name="Select", exact=True)

    def select_unit(self, unit_name: str):
        self.unit_select.click()
        self.page.get_by_role("searchbox", name="Search").fill(unit_name)
        self.page.get_by_text(unit_name, exact=True).click()
        return self
