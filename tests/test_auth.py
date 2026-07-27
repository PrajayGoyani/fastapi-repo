import pytest
from unittest.mock import patch, MagicMock

from app.services import auth as auth_service
from app.models.user import User
from app.core.limiter import limiter

from fastapi import status
from fastapi.testclient import TestClient
from app.main import app  # Replace with your actual app import
from app.core.config import settings

client = TestClient(app)

# Implemented test cases
"""
    1. test register success
    2. test register user already exist
    3. test login success
    4. test login user not found
    5. test login invalid password
    6. test rate limits on login and register routes
"""

USERNAME = "test.user"
PASSWORD = "12345"
FAKE_JWT = "fake.jwt.token"

@pytest.fixture
def mock_db_session():
    with patch("app.services.auth.get_db") as mock_get_db:
        session_mock = MagicMock()
        mock_get_db.side_effect = lambda: iter([session_mock])
        yield session_mock

@pytest.fixture
def mock_issue_jwt():
    with patch("app.services.auth.issue_jwt") as mock_jwt:
        mock_jwt.return_value = FAKE_JWT
        yield mock_jwt

def test_register_success(mock_db_session, mock_issue_jwt):
    mock_db_session.scalar.return_value = None
    
    def mock_refresh(instance):
        instance.id = 1
    mock_db_session.refresh.side_effect = mock_refresh

    response = auth_service.register(USERNAME, PASSWORD)

    assert response["message"] == "User registered!"
    assert response["data"]["access_token"] == FAKE_JWT
    assert response["data"]["user"]["username"] == USERNAME
    assert response["data"]["user"]["id"] == 1
    
    mock_db_session.add.assert_called_once()
    mock_db_session.commit.assert_called_once()
    mock_db_session.refresh.assert_called_once()


def test_register_user_already_exist(mock_db_session):
    mock_existing_user = MagicMock()
    mock_db_session.scalar.return_value = mock_existing_user

    with pytest.raises(BaseException) as exc_info:
        auth_service.register(USERNAME, PASSWORD)

    assert exc_info.value.status_code == 409
    assert exc_info.value.detail["message"] == "User already exists."

    mock_db_session.add.assert_not_called()
    mock_db_session.commit.assert_not_called()


def test_login_success(mock_db_session, mock_issue_jwt):
    fake_user = User(username=USERNAME)
    fake_user.id = 1

    fake_user.verify_password = MagicMock(return_value=True)

    mock_db_session.scalar.return_value = fake_user

    response = auth_service.login(USERNAME, PASSWORD)

    assert response["message"] == "User logged in!"
    assert response["data"]["user"]["id"] == 1
    assert response["data"]["user"]["username"] == USERNAME

def test_login_user_not_found(mock_db_session):
    mock_db_session.scalar.return_value = None

    with pytest.raises(BaseException) as exc_info:
        auth_service.login("fake.user", PASSWORD)

    assert exc_info.value.status_code == 401
    
    detail = exc_info.value.detail
    if isinstance(detail, dict):
        assert detail.get("message") == "Invalid credentials"
    else:
        assert "Invalid credentials" in str(detail)


def test_login_invalid_password(mock_db_session):
    mock_db_session.scalar.return_value = None

    with pytest.raises(BaseException) as exc_info:
        auth_service.login("fake.user", "wrong_password_123")

    assert exc_info.value.status_code == 401
    
    detail = exc_info.value.detail
    if isinstance(detail, dict):
        assert detail.get("message") == "Invalid credentials"
    else:
        assert "Invalid credentials" in str(detail)

def test_rate_limit(mock_db_session):
    limiter.enabled = True 
    payload = {"username": "rate.limit.user", "password": "password123"}
    headers = {"X-Forwarded-For": "127.0.0.1"}
    mock_db_session.scalar.return_value = None

    settings.AUTH_RATE_LIMIT = "2/minute"

    for _ in range(2):
        client.post("/auth/register", json=payload, headers=headers)
    
    th_response = client.post("/auth/register", json=payload, headers=headers)

    assert th_response.status_code == status.HTTP_429_TOO_MANY_REQUESTS
    assert "Rate limit exceeded" in th_response.text

    limiter.enabled = (settings.APP_ENV != "development")

