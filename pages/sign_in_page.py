import re

from playwright.sync_api import Page

from pages.base_page import BasePage


class SignInPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.organization_input = page.get_by_placeholder("Organization ID")
        self.email_input = page.get_by_placeholder("Email")
        self.password_input = page.get_by_placeholder("Password")
        self.sign_in_button = page.get_by_role("button", name="Sign In")

    def load(self):
        return self.goto("/en/sign-in")

    def select_organization(self, organization_id: str):
        self.organization_input.fill(organization_id)
        option = self.page.get_by_role("option").filter(
            has_text=re.compile(re.escape(organization_id), re.IGNORECASE)
        )
        option.first.click()
        return self

    def sign_in(self, organization_id: str, email: str, password: str):
        self.select_organization(organization_id)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.sign_in_button.click()
        return self
