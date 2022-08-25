from aiogram.dispatcher.filters.state import State, StatesGroup


class Help(StatesGroup):
    start = State()

    # Запрос помощи
    oborot = State()
    desc = State()