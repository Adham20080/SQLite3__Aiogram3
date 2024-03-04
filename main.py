import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command
from db import Database
from config import Token

dp = Dispatcher()
db = Database("db.db")


@dp.message(Command("start"))
async def start(message: Message):
    db.add_user(message.from_user.first_name, message.from_user.last_name, message.from_user.username,
                message.from_user.id)
    await message.answer("Xush keldingiz!")


async def main():
    bot = Bot(token=Token)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
