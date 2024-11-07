from aiogram import Bot, Router, types
from aiogram.filters import Command
from aiogram.types import Message

import asyncio

router = Router()

@router.message(Command("start"))
async def on_start(message: Message):
    await message.answer("Добро пожаловать в бота-помощника для чтения книг. Выберите один из пунктов.")
