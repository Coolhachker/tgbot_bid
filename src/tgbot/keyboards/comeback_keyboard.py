from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup, KeyboardButton

from src.Configs.text_of_buttons import TextOfButtons


def return_comeback_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    button_comeback = KeyboardButton(text=TextOfButtons.comeback_button)

    builder.row(button_comeback)

    return builder.as_markup(resize_keyboard=True)