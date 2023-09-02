import bcrypt
import pytest
from fastapi.testclient import TestClient
import time
from app import SessionLocal, app
from application.consts.api_consts import API_KEY, API_KEY_NAME

client = TestClient(app, 
                    base_url="http://localhost:8016",
                    headers={API_KEY_NAME : API_KEY})
timestamp = str(time.time())

# Mock object for tests
test_user_data = {
    "username": f"testuser_{timestamp}",
    "email": f"testuser_{timestamp}@example.com",
    "password": "testpassword",
    "connected_mail": "connected@example.com",
}

# Fixture for generating db connection
@pytest.fixture(scope="module")
def test_db():
    db = SessionLocal()
    yield db
    db.close()

# Testing endpoint for user creation
def test_create_user(test_db):
    password_hash = password_hash = bcrypt.hashpw(test_user_data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    test_user_data["password"] = password_hash
    response = client.post("/api/create-user", json=test_user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == test_user_data["username"]
    assert data["email"] == test_user_data["email"]

def test_get_user(test_db):
    username = test_user_data['username']
    response = client.get(f"/api/user?username={username}")
    assert response.status_code == 200
    user_data = response.json()
    assert user_data["username"] == test_user_data["username"]
    assert user_data["email"] == test_user_data["email"]

def test_valid_authentication():
    valid_credentials = {"username": test_user_data["username"], "password": test_user_data["password"]}
    url = f"/api/authenticate?username={valid_credentials['username']}&password={valid_credentials['password']}"
    response = client.post(url)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_modify_user(test_db):
    updated_data = {
        "new_username": f"newusername_{timestamp}",
        "new_email": f"newemail_{timestamp}@example.com",
        "new_connected_mail": "newconnected@example.com",
    }
    
    username = test_user_data['username']
    response = client.get(f"/api/user?username={username}")
    user = response.json()
    user_id = user['id']
    
    # Construct the URL with query parameters
    url = f"/api/modify-user/{user_id}?new_username={updated_data['new_username']}&new_email={updated_data['new_email']}&new_connected_mail={updated_data['new_connected_mail']}"
    
    response = client.put(url)
    assert response.status_code == 200
    user_data = response.json()
    assert user_data["username"] == updated_data["new_username"]
    assert user_data["email"] == updated_data["new_email"]
    assert user_data["connected_mail"] == updated_data["new_connected_mail"]


# def test_delete_user(test_db):
#     username = test_user_data['username']
#     response = client.get(f"/api/user?username={username}")
#     user = response.json()
#     user_id = user['id']

#     response = client.delete(f"/api/delete-user/{user_id}")
#     assert response.status_code == 200

def test_invalid_authentication():
    invalid_credentials = {"username": "testuser", "password": "wrongpassword"}
    url = f"/api/authenticate?username={invalid_credentials['username']}&password={invalid_credentials['password']}"
    response = client.post(url)
    assert response.status_code == 401