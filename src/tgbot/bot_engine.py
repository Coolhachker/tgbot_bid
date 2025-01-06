from aiogram import Bot, Dispatcher
from os import getenv
from dotenv import load_dotenv

from src.tgbot.middlewares.middleware_on_callback_request import MiddlewareOnCallback
load_dotenv()


class BotEngine:
    def __init__(self):
        self.bot = Bot(getenv('BOT_TOKEN'))
        self.dispatcher = Dispatcher()

    async def run(self):
        self.dispatcher.callback_query.middleware(MiddlewareOnCallback(self.bot))

    def run_sync_functions(self):
        pass
