import re

from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from aiogram.types import CallbackQuery
from aiogram import Bot

from src.Configs.templates import success_bid


class MiddlewareOnCallback(CallbackAnswerMiddleware):
    def __init__(self, bot: Bot):
        super().__init__()
        self.bot = bot

    async def __call__(self, handler, event: CallbackQuery, data):
        if re.search('Новая заявка', event.message.text) is None:
            await self.bot.delete_message(event.message.chat.id, event.message.message_id)
            await handler(event, data)
        else:
            await self.bot.delete_message(event.message.chat.id, event.message.message_id)
            await self.bot.send_message(event.message.chat.id, event.message.text+'\n'+success_bid)
            await handler(event, data)