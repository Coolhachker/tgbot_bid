from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton

from src.Configs.text_of_buttons import TextOfButtons
from src.Configs.callback_of_buttons import CallbacksOfButtons


def return_send_bid_keyboard(uniq_code: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    button_send_bid = InlineKeyboardButton(text=TextOfButtons.send_bid_button_text, callback_data=CallbacksOfButtons.callback_of_send_bid_button+uniq_code)

    builder.row(button_send_bid)

    return builder.as_markup()