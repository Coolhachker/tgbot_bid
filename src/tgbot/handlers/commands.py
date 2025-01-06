from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Bot, Dispatcher
from aiogram.fsm.context import FSMContext

from src.Configs.templates import hello_message, hello_admin

from src.tgbot.keyboards.send_bid_keyboard import return_send_bid_keyboard
from src.tgbot.keyboards.admin_keyboard import return_admin_keyboard

from src.Configs.States import States

from databases.sqlite3_db import client_sqlite3


def handle_commands(bot: Bot, dispatcher: Dispatcher):
    @dispatcher.message(CommandStart())
    async def handle_start_command(message: Message, state: FSMContext):
        client_sqlite3.add_user_into_table(message.chat.id, message.from_user.username, message.from_user.full_name)
        admins = client_sqlite3.get_admins()
        if message.from_user.username in admins[0]:
            client_sqlite3.update_admin(message.from_user.username, message.chat.id)
            await bot.send_message(message.chat.id, hello_admin, reply_markup=return_admin_keyboard())
        # else:
            await state.set_state(States.get_bio)
            await bot.send_message(message.chat.id, hello_message)

