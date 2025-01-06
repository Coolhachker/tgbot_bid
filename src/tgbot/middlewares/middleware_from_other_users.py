from aiogram import BaseMiddleware, Bot
from aiogram.types import Message

from src.Configs.templates import prohibition_message
from src.Configs.text_of_buttons import TextOfButtons

from databases.sqlite3_db import client_sqlite3


class MiddlewareFilterForAdmin(BaseMiddleware):
    def __init__(self, bot: Bot):
        super().__init__()
        self.bot = bot

    async def __call__(self, handler, event: Message, data):
        trust_users = client_sqlite3.get_admins()[0]

        if event.text == TextOfButtons.url_button or event.text == TextOfButtons.comeback_button:
            if event.from_user.username in trust_users:
                await handler(event, data)
            else:
                await self.bot.send_message(event.chat.id, prohibition_message)
        else:
            await handler(event, data)