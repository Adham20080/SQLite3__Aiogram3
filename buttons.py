from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup

key = [
    [types.KeyboardButton(text="Users"), types.KeyboardButton(text="Chats")],
]
keyboard = types.ReplyKeyboardMarkup(keyboard=key, resize_keyboard=True)

inline_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="My GitHub", url="https://github.com/Adham20080")]
])
