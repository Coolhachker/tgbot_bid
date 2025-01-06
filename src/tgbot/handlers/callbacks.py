from aiogram import Bot, Dispatcher
from aiogram.types import CallbackQuery
import re

from src.Configs.callback_of_buttons import CallbacksOfButtons
from src.Configs.templates import success_send_bid, new_bid

from src.tgbot.keyboards.response_on_bid_keyboard import return_response_on_bid_keyboard

from databases.sqlite3_db import client_sqlite3


def handle_callbacks(bot: Bot, dispatcher: Dispatcher):
    @dispatcher.callback_query(lambda cq: re.findall(CallbacksOfButtons.callback_of_send_bid_button, cq.data))
    async def handle_callback_of_send_bid_button(cq: CallbackQuery):
        uniq_code = cq.data.split(CallbacksOfButtons.callback_of_send_bid_button)[1]
        await bot.send_message(cq.message.chat.id, success_send_bid)


async def send_admins_the_new_bid(bot: Bot, uniq_code: str):
    admins = client_sqlite3.get_admins()
    user = client_sqlite3.get_user(uniq_code)
    for admin in admins:
        await bot.send_message(admin, new_bid % (user[1], user[2]), reply_markup=return_response_on_bid_keyboard(uniq_code))
