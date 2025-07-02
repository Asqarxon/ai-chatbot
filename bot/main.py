import asyncio

from aiogram.types import BotCommand
from shared.config import logger
from bot.handlers import dp, bot


async def set_bot_commands():
    """Set bot commands"""
    commands = [
        BotCommand(command="start", description="Start working with the bot"),
        BotCommand(command="clear", description="Clear conversation context"),
        BotCommand(command="help", description="Get help"),
    ]
    await bot.set_my_commands(commands)


async def main():
    logger.info("Starting Telegram bot...")

    await set_bot_commands()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
