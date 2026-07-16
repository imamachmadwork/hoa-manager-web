from playwright.sync_api import Page

from pages.base_page import BasePage


class RentalApplicationDetailPage(BasePage):
    """Reached by clicking a row on RentalApplicationPage's list, at
    /leasing/rental/{applicationId}.
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.heading = page.get_by_role("heading", name="Rental Application Details")
        self.overview_tab = page.get_by_role("tab", name="Overview")
        self.application_tab = page.get_by_role("tab", name="Application")
        self.files_tab = page.get_by_role("tab", name="Files")
        self.update_decision_button = page.get_by_role("button", name="Update Decision")
