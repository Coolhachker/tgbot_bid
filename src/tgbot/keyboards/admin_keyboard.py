from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup, KeyboardButton

from src.Configs.text_of_buttons import TextOfButtons


def return_admin_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    change_url_button = KeyboardButton(text=TextOfButtons.url_button)

    builder.row(change_url_button)

    return builder.as_markup(resize_keyboard=True)