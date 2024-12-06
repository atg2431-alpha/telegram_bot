from dotenv import load_dotenv
import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from models import model_llama

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

class Reference:
    """
    It stores previous response from the model
    """
    def __init__(self) -> None:
        self.reference = ""


reference = Reference()

dp = Dispatcher()
chat_memory={}

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    chat_id = message.chat.id

    if message.text == "/clear":
        chat_memory.pop(chat_id, None)
        await message.answer("Memory cleared!")
    else:
        if chat_id not in chat_memory:
            chat_memory[chat_id] = []
        chat_memory[chat_id].append(message.text)

        try:
            query = message.text
            response = model_llama.invoke(query)
            await message.answer(response.content)
        except:
            await message.answer("Nice try!")

        await message.answer(f"Stored messages for {chat_id}: {chat_memory[chat_id]}")

async def main() -> None:
    bot = Bot(token=TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())