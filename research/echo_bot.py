import logging
from aiogram import Bot, Dispatcher, types
from aiogram import executer
from dotenv import load_dotenv
import os

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# print(TELEGRAM_BOT_TOKEN)

logging.basicConfig(level=logging.INFO)

bot = Bot(token = TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)