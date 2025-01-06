from aiogram import BaseMiddleware, Bot
from aiogram.types import Message

from src.Configs.templates import is_invited_message

from databases.sqlite3_db import client_sqlite3


class MiddlewareFilterInvitedUsers(BaseMiddleware):
    def __init__(self, bot: Bot):
        super().__init__()
        self.bot = bot

    async def __call__(self, handler, event: Message, data):
        is_invited = client_sqlite3.invited_of_user(event.chat.id)
        try:
            if is_invited[0][0]:
                await self.bot.send_message(event.chat.id, is_invited_message)
            else:
                await handler(event, data)
        except IndexError:
            await handler(event, data)
