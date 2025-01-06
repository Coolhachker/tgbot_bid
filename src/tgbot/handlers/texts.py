from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from src.Configs.text_of_buttons import TextOfButtons
from src.Configs.templates import url_message, success_comeback_message

from src.tgbot.keyboards.change_url_keyboard import return_change_url_keyboard
from src.tgbot.keyboards.admin_keyboard import return_admin_keyboard

from databases.sqlite3_db import client_sqlite3


def handle_texts(bot: Bot, dispatcher: Dispatcher):
    @dispatcher.message(lambda message: message.text == TextOfButtons.url_button)
    async def handle_change_url_button(message: Message):
        url_of_chat = client_sqlite3.get_url_of_chat()
        await bot.send_message(message.chat.id, url_message % url_of_chat, reply_markup=return_change_url_keyboard())

    @dispatcher.message(lambda message: message.text == TextOfButtons.comeback_button)
    async def handle_comeback_button(message: Message, state: FSMContext):
        await state.clear()
        await bot.send_message(message.chat.id, success_comeback_message, reply_markup=return_admin_keyboard())