import pytest
from httpx import AsyncClient
from backend.main import app


@pytest.mark.asyncio
async def test_end_to_end_conversation_flow():
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Step 1: Send message
        response = await client.post("/api/v1/chat", json={
            "user_id": 5555,
            "message": "Hello AI!",
            "username": "tester"
        })
        assert response.status_code == 200
        assert "response" in response.json()

        # Step 2: Get conversation history
        history = await client.get("/api/v1/conversations/5555/history")
        assert history.status_code == 200
        assert "history" in history.json()

        # Step 3: Clear conversation
        clear = await client.delete("/api/v1/conversations/5555")
        assert clear.status_code == 200
