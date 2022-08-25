from aiogram.dispatcher.filters.state import State, StatesGroup


class Tinder(StatesGroup):
    started = State()

    # Отзывы
    feedback = State()
    desc = State()

    # Фильтры поиска
    city = State()
    industri = State()
    region = State()
    hobbi = State()

    # Кнопка связаться
    connect = State()
