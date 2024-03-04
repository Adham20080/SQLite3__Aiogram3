import asyncio
import logging
from buttons import keyboard
from db import Database
from config import Token, Admin
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters.command import Command

dp = Dispatcher()
db = Database("db.db")


@dp.message(Command("start"))
async def start(message: Message):
    if message.from_user.id == Admin:
        await message.answer("Xush keldingiz admin janoblari!", reply_markup=keyboard)
    else:
        db.add_user(message.from_user.first_name, message.from_user.last_name, message.from_user.username,
                    message.from_user.id)
        await message.answer("Xush keldingiz botimizga!")


@dp.message(F.text == "Users")
async def users(message: Message):
    if message.from_user.id == Admin:
        for i in db.get_all_users:
            await message.answer(f"Key ID: <b>{i[0]}</b>\nName: <b>{i[1]}</b>\nSurname: <b>{i[2]}</b>\nUsername: <b>{i[3]}</b>\nUser ID: <b>{i[4]}</b>",
                                 parse_mode="HTML")


async def main():
    bot = Bot(token=Token)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
