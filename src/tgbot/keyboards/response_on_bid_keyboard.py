from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton

from src.Configs.text_of_buttons import TextOfButtons
from src.Configs.callback_of_buttons import CallbacksOfButtons


def return_response_on_bid_keyboard(uniq_code: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    response_button = InlineKeyboardButton(text=TextOfButtons.response_bid_button, callback_data=CallbacksOfButtons.callback_of_response_bid_button+uniq_code)

    builder.row(response_button)

    return builder.as_markup()