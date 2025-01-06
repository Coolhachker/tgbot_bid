from aiogram import Bot, Dispatcher
from os import getenv
from dotenv import load_dotenv

from src.tgbot.middlewares.middleware_on_callback_request import MiddlewareOnCallback
from src.tgbot.middlewares.middleware_from_other_users import MiddlewareFilterForAdmin
from src.tgbot.middlewares.middleware_on_invited_users import MiddlewareFilterInvitedUsers

from src.tgbot.handlers import callbacks, commands, texts, states
load_dotenv()


class BotEngine:
    def __init__(self):
        self.bot = Bot(getenv('BOT_TOKEN'))
        self.dispatcher = Dispatcher()

        self.run_sync_functions()

    async def run(self):
        self.dispatcher.callback_query.middleware(MiddlewareOnCallback(self.bot))
        self.dispatcher.message.middleware(MiddlewareFilterInvitedUsers(self.bot))
        self.dispatcher.message.middleware(MiddlewareFilterForAdmin(self.bot))

        await self.dispatcher.start_polling(self.bot)

    def run_sync_functions(self):
        commands.handle_commands(self.bot, self.dispatcher)
        texts.handle_texts(self.bot, self.dispatcher)
        callbacks.handle_callbacks(self.bot, self.dispatcher)
        states.handle_states(self.bot, self.dispatcher)
