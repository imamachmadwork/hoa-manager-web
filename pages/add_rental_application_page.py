from playwright.sync_api import Page

from pages.base_page import BasePage


class AddRentalApplicationPage(BasePage):
    """The 'Add Rental Application' modal, reached from
    RentalApplicationPage.start_add_application().
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.dialog = page.locator("app-add-rental-application")
        self.dialog_heading = self.dialog.get_by_role("heading", name="Add Rental Application")

        # "Prospect" section - not exercised by tests: opens a contact-picker
        # sub-dialog, the same shape as the Add Lease wizard's Select Tenant
        # dialog, which creates real contact records.
        self.add_prospect_button = self.dialog.get_by_role("button", name="Add Prospect")

        # "Application Information" section
        self.association_select = page.get_by_label("Select Association")
        self.unit_select = page.get_by_label("Select Unit")
        self.assigned_to_select = page.get_by_label("Select Assigned To")
        self.desired_move_in_input = page.get_by_label("Desired Move-in")
        self.specify_fees_toggle = self.dialog.get_by_text("Specify fees for this application")

        self.cancel_button = self.dialog.get_by_role("button", name="Cancel", exact=True)
        self.save_button = self.dialog.get_by_role("button", name="Save", exact=True)
