"""
Helpers - ENKEL VERSION
Bara hjälpfunktioner som faktiskt behövs
"""

from playwright.sync_api import Page


def take_screenshot(page: Page, name: str):
    """Ta screenshot"""
    filename = f"screenshots/{name}.png"
    page.screenshot(path=filename)
    print(f"Screenshot sparad: {filename}")


def wait_for_element(page: Page, selector: str, timeout: int = 5000):
    """Vänta på element"""
    try:
        page.wait_for_selector(selector, timeout=timeout)
        return True
    except:
        return False


def get_element_text(page: Page, selector: str) -> str:
    """Hämta text från element"""
    try:
        return page.text_content(selector)
    except:
        return ""


def is_element_visible(page: Page, selector: str) -> bool:
    """Är element synlig?"""
    try:
        page.wait_for_selector(selector, timeout=2000)
        return True
    except:
        return False
