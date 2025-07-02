import pytest
from aiogram.types import Message
from bot.handlers import start_handler, help_handler, clear_handler
from aiogram.fsm.context import FSMContext
from unittest.mock import AsyncMock


@pytest.mark.asyncio
async def test_start_handler():
    message = AsyncMock(spec=Message)
    state = AsyncMock(spec=FSMContext)
    await start_handler(message, state)
    message.answer.assert_called_once()
    state.set_state.assert_called_once()


@pytest.mark.asyncio
async def test_help_handler():
    message = AsyncMock(spec=Message)
    state = AsyncMock(spec=FSMContext)
    await help_handler(message, state)
    message.answer.assert_called_once()
    state.set_state.assert_called_once()
