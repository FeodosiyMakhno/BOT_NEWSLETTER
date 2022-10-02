from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from main import dp,bot
from config import users,id_admin

@dp.message_handler(Command('sendall'))
async def send_all(message: Message):
    if message.chat.id == id_admin:
        await message.answer("Start")
        for i in users:
            await bot.send_message(i,message.text[message.text.find(' '):])

        await  message.answer('Done')

@dp.message_handler(Command('sendallwp'))
async def send_all(message: Message):
    if message.chat.id == id_admin:
        await message.answer("Start")
        for i in users:
            await bot.send_photo(i,open('images .jpg','rb'),message.text[message.text.find(' '):])

        await  message.answer('Done')