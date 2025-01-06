from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Bot, Dispatcher

from src.Configs.templates import hello_message
from src.tgbot.keyboards.send_bid_keyboard import return_send_bid_keyboard

from databases.sqlite3_db import client_sqlite3


def handle_commands(bot: Bot, dispatcher: Dispatcher):
    @dispatcher.message(CommandStart())
    async def handle_start_command(message: Message):
        client_sqlite3.add_user_into_table(message.chat.id, message.from_user.usernam, message.from_user.full_name)
        uniq_code = client_sqlite3.get_uniq_code_of_user(message.chat.id)

        await bot.send_message(message.chat.id, hello_message, reply_markup=return_send_bid_keyboard(uniq_code))
