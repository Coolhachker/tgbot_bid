from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton

from src.Configs.text_of_buttons import TextOfButtons
from src.Configs.callback_of_buttons import CallbacksOfButtons


def return_change_url_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    change_button = InlineKeyboardButton(text=TextOfButtons.change_url_button, callback_data=CallbacksOfButtons.callback_of_change_url_button)

    builder.row(change_button)

    return builder.as_markup()