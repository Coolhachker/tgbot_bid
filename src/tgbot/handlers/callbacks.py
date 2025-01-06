import aiogram.exceptions
from aiogram import Bot, Dispatcher
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from src.Configs.callback_of_buttons import CallbacksOfButtons
from src.Configs.templates import success_send_bid, new_bid, write_url_message, success_response_from_bid
from src.Configs.States import States

from src.tgbot.keyboards.response_on_bid_keyboard import return_response_on_bid_keyboard
from src.tgbot.keyboards.comeback_keyboard import return_comeback_keyboard

from databases.sqlite3_db import client_sqlite3


def handle_callbacks(bot: Bot, dispatcher: Dispatcher):
    @dispatcher.callback_query(lambda cq: cq.data.startswith(CallbacksOfButtons.callback_of_send_bid_button))
    async def handle_callback_of_send_bid_button(cq: CallbackQuery):
        uniq_code = cq.data.split(CallbacksOfButtons.callback_of_send_bid_button)[1]
        await bot.send_message(cq.message.chat.id, success_send_bid)
        await send_admins_the_new_bid(bot, uniq_code)

    @dispatcher.callback_query(lambda cq: cq.data.startswith(CallbacksOfButtons.callback_of_response_bid_button))
    async def handle_callback_of_response_bid_button(cq: CallbackQuery):
        uniq_code = cq.data.split(CallbacksOfButtons.callback_of_response_bid_button)[1]

        user = client_sqlite3.get_user(uniq_code)
        chat_id_of_user = user[0]
        url = client_sqlite3.get_url_of_chat()

        if user[4] == 0:
            client_sqlite3.update_invited_of_user(chat_id_of_user)
            await bot.send_message(chat_id_of_user, success_response_from_bid % url)

    @dispatcher.callback_query(lambda cq: cq.data == CallbacksOfButtons.callback_of_change_url_button)
    async def handle_callback_of_change_url_button(cq: CallbackQuery, state: FSMContext):
        await state.set_state(States.get_url)
        await bot.send_message(cq.message.chat.id, write_url_message, reply_markup=return_comeback_keyboard())


async def send_admins_the_new_bid(bot: Bot, uniq_code: str):
    admins = client_sqlite3.get_admins()
    user = client_sqlite3.get_user(uniq_code)
    for admin in admins[1]:
        try:
            await bot.send_message(admin, new_bid % (user[1], user[2]) + '\n' + user[3], reply_markup=return_response_on_bid_keyboard(uniq_code), parse_mode='html')
        except aiogram.exceptions.TelegramBadRequest:
            continue
