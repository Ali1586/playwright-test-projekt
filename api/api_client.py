import requests
import os
from typing import Dict, Any

class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.headers = {"Content-Type": "application/json"}
        self.token = None
    
    def login(self, username: str, password: str) -> Dict[str, Any]:
        """Logga in och få token"""
        response = requests.post(
            f"{self.base_url}/login",
            json={"username": username, "password": password},
            headers=self.headers
        )
        assert response.status_code == 200, f"Login failed: {response.text}"
        data = response.json()
        self.token = data.get("token")
        return data
    
    def get_users(self) -> Dict[str, Any]:
        """Hämta alla användare"""
        headers = self.headers.copy()
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        
        response = requests.get(
            f"{self.base_url}/users",
            headers=headers
        )
        assert response.status_code == 200
        return response.json()
    
    def create_user(self, username: str, email: str, password: str) -> Dict[str, Any]:
        """Skapa ny användare"""
        response = requests.post(
            f"{self.base_url}/users",
            json={"username": username, "email": email, "password": password},
            headers=self.headers
        )
        assert response.status_code == 201
        return response.json()
    
    def delete_user(self, user_id: int) -> None:
        """Ta bort användare"""
        headers = self.headers.copy()
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        
        response = requests.delete(
            f"{self.base_url}/users/{user_id}",
            headers=headers
        )
        assert response.status_code == 204
