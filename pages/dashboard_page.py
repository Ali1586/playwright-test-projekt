"""
Dashboard Page - ENKEL VERSION
Mycket grundläggande utan allt för mycket kod
"""

from playwright.sync_api import Page


class DashboardPage:
    """Hanterar dashboard-sidan - ENKEL VERSION"""

    def __init__(self, page: Page):
        """Initialisera sidan"""
        self.page = page

    # ==================== GOTOER ====================
    def goto_dashboard(self):
        """Gå till dashboard"""
        self.page.goto("http://localhost:3000/dashboard")
        self.page.wait_for_load_state("networkidle")

    def goto_products(self):
        """Gå till produkter"""
        self.page.goto("http://localhost:3000/products")
        self.page.wait_for_load_state("networkidle")

    # ==================== KLICKNINGAR ====================
    def click_logout(self):
        """Klicka logout"""
        self.page.click("button:has-text('Logout')")

    def click_cart(self):
        """Klicka på kundvagn"""
        self.page.click("[data-testid='cart-icon']")

    def click_profile(self):
        """Klicka på profil"""
        self.page.click("[data-testid='profile']")

    # ==================== KONTROLLER ====================
    def is_logged_in(self) -> bool:
        """Är användaren inloggad?"""
        try:
            self.page.wait_for_selector("h1:has-text('Dashboard')", timeout=5000)
            return True
        except:
            return False

    def is_page_loaded(self) -> bool:
        """Är sidan laddad?"""
        return "dashboard" in self.page.url.lower()