from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    return browser.new_page()

def test_successful_login(page):
    """Test login med giltiga uppgifter"""
    page.goto("https://www.saucedemo.com/")
    
    # Fylla email-fält#
    page.fill("#user-name", "standard_user")
    
    # Fylla password-fält
    page.fill("#password", "secret_sauce")
    
    # Klicka login-button
    page.click("#login-button")
    
    # Vänta på och verifiera dashboard
    page.wait_for_selector(".title")
    assert page.is_visible(".title")
    
    print("✅ Login test PASSED")

def test_invalid_login(page):
    """Test login med felaktig lösenord"""
    page.goto("https://www.saucedemo.com/")
    
    page.fill("#user-name", "standard_user")
    page.fill("#password", "wrong_password")
    page.click("#login-button")
    
    # Verifiera error-meddelande
    assert page.is_visible(".error-message-container")
    error_text = page.text_content(".error-message-container")
    assert "Username and password do not match" in error_text
    
    print("✅ Error handling test PASSED")
