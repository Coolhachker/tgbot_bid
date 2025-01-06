from aiogram.fsm.state import State, StatesGroup


class States(StatesGroup):
    get_url = State()
    get_bio = State()