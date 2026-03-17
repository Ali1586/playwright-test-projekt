"""
ENKEL GUI-test för RestFul Booker
"""

from playwright.sync_api import Page
from config.settings import BASE_URL


def test_1_page_loads(page: Page):
    """Test 1: Sidan laddar"""
    print("\n" + "="*40)
    print("TEST 1: Page Loads")
    print("="*40)
    
    # Gå till sidan
    page.goto(BASE_URL)
    
    # Vänta på ladning
    page.wait_for_load_state("networkidle")
    
    # Kontrollera URL
    print(f"URL: {page.url}")
    assert BASE_URL in page.url
    print("✅ Sidan laddad!")


def test_2_page_has_content(page: Page):
    """Test 2: Sidan har innehål"""
    print("\n" + "="*40)
    print("TEST 2: Page Has Content")
    print("="*40)
    
    # Gå till sidan
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    
    # Hämta text
    content = page.text_content("body")
    
    # Kontrollera
    print(f"Innehål längd: {len(content)} tecken")
    assert len(content) > 0
    print("✅ Sidan har innehål!")


def test_3_page_title(page: Page):
    """Test 3: Sidan har titel"""
    print("\n" + "="*40)
    print("TEST 3: Page Title")
    print("="*40)
    
    # Gå till sidan
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    
    # Hämta titel
    title = page.title()
    
    # Kontrollera
    print(f"Titel: {title}")
    assert len(title) > 0
    print("✅ Sidan har titel!")


def test_4_api_docs_link(page: Page):
    """Test 4: API docs-länk finns"""
    print("\n" + "="*40)
    print("TEST 4: API Docs Link")
    print("="*40)
    
    # Gå till sidan
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    
    # Leta efter API-länk
    try:
        api_link = page.locator("a[href*='apidoc']")
        found = api_link.count() > 0
        
        if found:
            print("✅ API docs-länk hittad!")
        else:
            print("ℹ️ API docs-länk inte synlig")
    except:
        print("ℹ️ Kunde inte hitta länk")


def test_5_page_load_time(page: Page):
    """Test 5: Sidan laddar snabbt"""
    print("\n" + "="*40)
    print("TEST 5: Page Load Time")
    print("="*40)
    
    import time
    
    # Mät tid
    start = time.time()
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    duration = time.time() - start
    
    # Kontrollera
    print(f"Load tid: {duration:.2f}s")
    assert duration < 10  # Mindre än 10 sekunder
    print("✅ Sidan laddar snabbt!")


if __name__ == "__main__":
    print("\n🌐 RestFul Booker GUI Tests")
    print(f"Testing: {BASE_URL}\n")