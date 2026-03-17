"""
Products Page - ENKEL VERSION
Mycket grundläggande utan allt för mycket kod
"""

from playwright.sync_api import Page


class ProductsPage:
    """Hanterar produktsidan - ENKEL VERSION"""

    def __init__(self, page: Page):
        """Initialisera sidan"""
        self.page = page

    # ==================== NAVIGERING ====================
    def goto_products(self):
        """Gå till produktsidan"""
        self.page.goto("http://localhost:3000/products")
        self.page.wait_for_load_state("networkidle")

    # ==================== SÖKNINGAR ====================
    def search(self, product_name: str):
        """Sök efter produkt"""
        self.page.fill("input[placeholder='Search']", product_name)
        self.page.press("input[placeholder='Search']", "Enter")
        self.page.wait_for_load_state("networkidle")

    # ==================== FILTRERING ====================
    def filter_by_price(self, min_price: str, max_price: str):
        """Filtrera pris"""
        self.page.fill("input[data-testid='price-min']", min_price)
        self.page.fill("input[data-testid='price-max']", max_price)
        self.page.click("button:has-text('Filter')")
        self.page.wait_for_load_state("networkidle")

    # ==================== KUNDVAGN ====================
    def add_to_cart(self, product_index: int = 0):
        """Lägg till produkt i cart"""
        products = self.page.locator("[data-testid='product-item']")
        products.nth(product_index).locator("button:has-text('Add')").click()
        self.page.wait_for_timeout(500)

    # ==================== KONTROLLER ====================
    def get_product_count(self) -> int:
        """Hur många produkter visas?"""
        products = self.page.locator("[data-testid='product-item']")
        return products.count()

    def is_page_loaded(self) -> bool:
        """Är produktsidan laddad?"""
        return "products" in self.page.url.lower()

    def has_no_results(self) -> bool:
        """Visar "no results"?"""
        try:
            self.page.wait_for_selector("text=No products found", timeout=2000)
            return True
        except:
            return False