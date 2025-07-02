import pytest
from httpx import AsyncClient
from backend.main import app


@pytest.mark.asyncio
async def test_chat_endpoint_returns_response():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/v1/chat", json={
            "user_id": 123456,
            "message": "What is a Python decorator?",
            "username": "test_user"
        })
        assert response.status_code == 200
        data = response.json()
        assert "response" in data
        assert isinstance(data["response"], str)
