import pytest

@pytest.mark.asyncio
async def test_register_and_login(client):
    # Test Register
    reg_payload = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "securepassword123"
    }
    response = await client.post("/api/v1/auth/register", json=reg_payload)
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "testuser"
    assert "id" in data

    # Test Login
    login_payload = {
        "username": "testuser",
        "password": "securepassword123"
    }
    response = await client.post("/api/v1/auth/login", data=login_payload)
    assert response.status_code == 200
    token_data = response.json()
    assert "access_token" in token_data
    assert token_data["token_type"] == "bearer"
