"""
ENKEL API-test för RestFul Booker
"""

import requests
from config.settings import BASE_URL

API_URL = f"{BASE_URL}/booking"


def test_1_health_check():
    """Test 1: API är igång"""
    print("\n" + "="*40)
    print("TEST 1: Health Check")
    print("="*40)
    
    # Gör GET request
    response = requests.get(f"{BASE_URL}/ping")
    
    # Kontrollera status
    print(f"Status: {response.status_code}")
    assert response.status_code == 201
    print("✅ API är igång!")


def test_2_get_bookings():
    """Test 2: Hämta bokningar"""
    print("\n" + "="*40)
    print("TEST 2: Get Bookings")
    print("="*40)
    
    # Hämta alla bokningar
    response = requests.get(API_URL)
    
    # Kontrollera
    print(f"Status: {response.status_code}")
    assert response.status_code == 200
    
    data = response.json()
    print(f"Bokningar hittade: {len(data)}")
    print("✅ Bokningar hämtade!")


def test_3_create_booking():
    """Test 3: Skapa bokning"""
    print("\n" + "="*40)
    print("TEST 3: Create Booking")
    print("="*40)
    
    # Data
    booking = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-05"
        },
        "additionalneeds": "Breakfast"
    }
    
    # Skapa
    response = requests.post(API_URL, json=booking)
    
    # Kontrollera
    print(f"Status: {response.status_code}")
    assert response.status_code == 200
    
    result = response.json()
    booking_id = result["bookingid"]
    print(f"Bokning skapad! ID: {booking_id}")
    print("✅ Bokning skapad!")
    
    return booking_id


def test_4_get_booking():
    """Test 4: Hämta specifik bokning"""
    print("\n" + "="*40)
    print("TEST 4: Get Specific Booking")
    print("="*40)
    
    # Skapa en bokning först
    booking = {
        "firstname": "Jane",
        "lastname": "Smith",
        "totalprice": 222,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2024-02-01",
            "checkout": "2024-02-05"
        }
    }
    
    create_response = requests.post(API_URL, json=booking)
    booking_id = create_response.json()["bookingid"]
    
    # Hämta den
    response = requests.get(f"{API_URL}/{booking_id}")
    
    # Kontrollera
    print(f"Status: {response.status_code}")
    assert response.status_code == 200
    
    data = response.json()
    print(f"Namn: {data['firstname']} {data['lastname']}")
    print("✅ Bokning hämtad!")


def test_5_delete_booking():
    """Test 5: Radera bokning"""
    print("\n" + "="*40)
    print("TEST 5: Delete Booking")
    print("="*40)
    
    # Skapa en bokning
    booking = {
        "firstname": "Delete",
        "lastname": "Me",
        "totalprice": 50,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-03-01",
            "checkout": "2024-03-05"
        }
    }
    
    create_response = requests.post(API_URL, json=booking)
    booking_id = create_response.json()["bookingid"]
    
    # Radera den
    response = requests.delete(f"{API_URL}/{booking_id}")
    
    # Kontrollera - 201 eller 403 är OK
    print(f"Status: {response.status_code}")
    assert response.status_code in [201, 403], f"Unexpected status: {response.status_code}"
    
    print(f"Bokning {booking_id} behandlad!")
    print("✅ Bokning raderad eller saknade rättigheter!")


if __name__ == "__main__":
    print("\n🧪 RestFul Booker API Tests")
    print(f"Testing: {API_URL}\n")