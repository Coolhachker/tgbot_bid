from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

import re

from src.Configs.States import States
from src.Configs.templates import incorrect_url, success_save_url, success_write_bio

from src.tgbot.keyboards.send_bid_keyboard import return_send_bid_keyboard


from src.tgbot.keyboards.admin_keyboard import return_admin_keyboard

from databases.sqlite3_db import client_sqlite3


def handle_states(bot: Bot, dispatcher: Dispatcher):
    @dispatcher.message(States.get_url)
    async def handle_state_get_url(message: Message, state: FSMContext):
        if len(re.findall('/', message.text)) == 3:
            await state.clear()
            client_sqlite3.update_url_of_chat(message.text)

            await bot.send_message(message.chat.id, success_save_url, reply_markup=return_admin_keyboard())
        else:
            await bot.send_message(message.chat.id, incorrect_url)

    @dispatcher.message(States.get_bio)
    async def handle_state_get_bio(message: Message, state: FSMContext):
        await state.clear()
        client_sqlite3.update_bio_of_user(message.text, message.chat.id)
        uniq_code = client_sqlite3.get_uniq_code_of_user(message.chat.id)

        await bot.send_message(message.chat.id, success_write_bio, reply_markup=return_send_bid_keyboard(uniq_code))
