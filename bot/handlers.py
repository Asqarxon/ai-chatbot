import httpx

from aiogram.types import Message
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from bot.states import ConversationState
from shared.config import config, logger

bot = Bot(token=config.TELEGRAM_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message, state: FSMContext):
    await message.answer(
        "🤖 Hello! I'm an AI assistant here to help you with programming.\n\n"
        "Available commands:\n"
        "/start - Start\n"
        "/help - Get help\n"
        "/clear - Clear conversation context\n\n"
        "Just send your question and I’ll do my best to help!"
    )
    await state.set_state(ConversationState.waiting_for_message)


@dp.message(Command("help"))
async def help_handler(message: Message, state: FSMContext):
    """Handles the /help command"""
    await message.answer(
        "🆘 Help:\n\n"
        "I can help you with:\n"
        "• Explaining programming concepts\n"
        "• Debugging code\n"
        "• Architecture recommendations\n"
        "• Answering technical questions\n\n"
        "Just send your question."
    )
    await state.set_state(ConversationState.waiting_for_message)


@dp.message(Command("clear"))
async def clear_handler(message: Message, state: FSMContext):
    """Clear conversation context"""
    user_id = message.from_user.id
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"{config.BACKEND_URL}/api/v1/conversations/{user_id}",
                timeout=10.0
            )
            if response.status_code == 200:
                await message.answer("🗑 Conversation context cleared.")
            else:
                await message.answer("⚠️ Failed to clear conversation context.")
    except Exception as e:
        logger.error(f"Error clearing context: {e}")
        await message.answer("❌ An error occurred while clearing context.")
    finally:
        await state.set_state(ConversationState.waiting_for_message)


@dp.message(ConversationState.waiting_for_message)
async def message_handler(message: Message, state: FSMContext):
    """Handles user messages"""
    user_id = message.from_user.id
    user_message = message.text

    # Show 'typing...' status
    await bot.send_chat_action(message.chat.id, "typing")

    try:
        # Send request to backend
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{config.BACKEND_URL}/api/v1/chat",
                json={
                    "user_id": user_id,
                    "message": user_message,
                    "username": message.from_user.username or "Unknown"
                },
                timeout=30.0
            )

            if response.status_code == 200:
                data = response.json()
                ai_response = data.get("response", "Failed to get response.")

                # Split long messages
                if len(ai_response) > 4000:
                    chunks = [ai_response[i:i + 4000] for i in range(0, len(ai_response), 4000)]
                    for chunk in chunks:
                        await message.answer(chunk)
                else:
                    await message.answer(ai_response)
            else:
                await message.answer("❌ Error while processing the request.")

    except httpx.TimeoutException:
        await message.answer("⏱ Timeout. Please try again.")
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        await message.answer("❌ An error occurred. Please try again later.")
