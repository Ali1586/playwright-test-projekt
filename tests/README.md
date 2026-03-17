"""
================================================
RESTFUL BOOKER - ENKELT PROJEKT
================================================

https://restful-booker.herokuapp.com/
"""

# ============================================================================
# QUICK START - 3 MINUTER
# ============================================================================

"""
STEG 1: Installera
──────────────────
pip install requests playwright pytest python-dotenv
playwright install

STEG 2: Kör API-tester
──────────────────────
pytest tests/test_api_simple.py -v -s

STEG 3: Kör GUI-tester
──────────────────────
pytest tests/test_gui_simple.py -v -s

STEG 4: Kör allt
────────────────
pytest tests/ -v -s

Det är det! ✅
"""

# ============================================================================
# VAD GÖR VARJE TEST?
# ============================================================================

"""
API TESTS (test_api_simple.py):
───────────────────────────────

test_1_health_check
  → Kontrollera att API är igång
  → GET /ping

test_2_get_bookings
  → Hämta alla bokningar
  → GET /booking

test_3_create_booking
  → Skapa ny bokning
  → POST /booking

test_4_get_booking
  → Hämta specifik bokning
  → GET /booking/{id}

test_5_delete_booking
  → Radera en bokning
  → DELETE /booking/{id}

═══════════════════════════════════════════════════════════════

GUI TESTS (test_gui_simple.py):
───────────────────────────────

test_1_page_loads
  → Sidan laddar

test_2_page_has_content
  → Sidan har innehål

test_3_page_title
  → Sidan har titel

test_4_api_docs_link
  → API docs-länk finns

test_5_page_load_time
  → Sidan laddar snabbt
"""

# ============================================================================
# RESULTAT
# ============================================================================

"""
Når du kör: pytest tests/ -v -s

Du ska se:

tests/test_api_simple.py::test_1_health_check PASSED
tests/test_api_simple.py::test_2_get_bookings PASSED
tests/test_api_simple.py::test_3_create_booking PASSED
tests/test_api_simple.py::test_4_get_booking PASSED
tests/test_api_simple.py::test_5_delete_booking PASSED
tests/test_gui_simple.py::test_1_page_loads PASSED
tests/test_gui_simple.py::test_2_page_has_content PASSED
tests/test_gui_simple.py::test_3_page_title PASSED
tests/test_gui_simple.py::test_4_api_docs_link PASSED
tests/test_gui_simple.py::test_5_page_load_time PASSED

===== 10 passed in 15.23s =====

✅ ALLA TESTER PASSAR!
"""

# ============================================================================
# FILER
# ============================================================================

"""
.env
  → BASE_URL (bara denna!)

config/settings.py
  → Läser BASE_URL från .env

tests/test_api_simple.py
  → 5 enkla API-tester

tests/test_gui_simple.py
  → 5 enkla GUI-tester
"""

# ============================================================================
# NÄSTA STEG
# ============================================================================

"""
NU KAN DU:

1. Lägg till fler API-tester
   → test_update_booking
   → test_invalid_data
   → test_duplicate_booking

2. Lägg till fler GUI-tester
   → test_responsive_design
   → test_no_errors
   → test_links_work

3. Ändr test-data
   → Justera firstname, lastname
   → Ändr datum
   → Ändr priser

4. Testa fel-fall
   → DELETE med fel ID
   → POST med saknad data
   → GET med felaktig ID

5. Skapa fixtures för setup
   → Skapa bokning innan test
   → Rensa upp efter test
"""

# ============================================================================
# TIPS
# ============================================================================

"""
💡 ENKLA TIPS:

1. Läs felmeddelande noga
   Säger vad som gick fel

2. Använd -s flag för att se print
   pytest tests/ -s

3. Testa ett test i taget
   pytest tests/test_api_simple.py::test_1_health_check -v -s

4. Lägg till print i tester
   print(f"Booking ID: {booking_id}")

5. Kolla response data
   print(response.json())

6. Öppna URL i webläsare
   https://restful-booker.herokuapp.com/

7. Läs API-dokumentation
   https://restful-booker.herokuapp.com/apidoc/index.html
"""

# ============================================================================
# LYCKA TILL!
# ============================================================================

"""
Du har nu:

✅ 5 enkla API-tester
✅ 5 enkla GUI-tester
✅ Enkel konfiguration
✅ Enkla instruktioner

Kör: pytest tests/ -v -s

Lycka till! 🚀
"""

print(__doc__)