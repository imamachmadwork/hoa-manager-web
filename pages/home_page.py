from playwright.sync_api import Page

from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.main_heading = page.get_by_role("heading", level=1)
        self.get_started_link = page.get_by_role("link", name="Get Started").first

    def load(self):
        return self.goto("/")
