"""
Conftest - ENKEL VERSION
Minimal setup för pytest
"""

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def browser():
    """Skapar browser"""
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    
    yield browser
    
    browser.close()
    playwright.stop()


@pytest.fixture
def page(browser):
    """Skapar page"""
    context = browser.new_context()
    page = context.new_page()
    
    yield page
    
    page.close()
    context.close()