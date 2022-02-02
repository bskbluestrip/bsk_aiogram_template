from audioop import add
import sqlite3
from aiogram import types
from aiogram.types import Message
from loader import dp 
from utils.db_api.dp import newbie_db, check_newbie


connect = sqlite3.connect('database.db') 
cursor = connect.cursor()

@dp.message_handler(text="/start")
async def onstart(message: Message):
    if await check_newbie(message.from_user.id) is False:

        if await newbie_db(message.from_user.id, message.from_user.full_name) is True:
            await message.answer(f"Добро пожаловать {message.from_user.full_name}🏧")
        else:
            await message.answer(f"Возникла какая то ошибка ⛔")
    else:
        await message.answer(f"С возращением, {message.from_user.full_name} 🏧")