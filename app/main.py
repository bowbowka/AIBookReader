from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
import asyncio
# pip install python-dotenv
# импортируем BOT_TOKEN из .env
# хз так чат жпт написал...

import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def on_start(message: Message):
    await message.answer("Добро пожаловать в нашего бота")

async def main():
     await dp.start_polling(bot)

if __name__ == "__main__":
     asyncio.run(main())