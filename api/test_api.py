import pytest
from api.api_client import APIClient

@pytest.fixture
def api_client():
    return APIClient("https://api.example.com")

def test_create_and_get_user(api_client):
    """Test att skapa och hämta användare"""
    # Skapa användare
    user_data = api_client.create_user(
        username="testuser",
        email="test@example.com",
        password="secure123"
    )
    
    assert user_data["username"] == "testuser"
    assert user_data["id"] is not None
    
    # Hämta användare
    users = api_client.get_users()
    assert any(u["username"] == "testuser" for u in users)
    
    print("✅ Create and get user test PASSED")

def test_login_and_auth(api_client):
    """Test autentisering"""
    login_response = api_client.login("testuser", "secure123")
    
    assert "token" in login_response
    assert api_client.token is not None
    
    print("✅ Login and auth test PASSED")
