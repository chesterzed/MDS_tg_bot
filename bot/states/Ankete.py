from aiogram.dispatcher.filters.state import State, StatesGroup


class Anketa(StatesGroup):
    # Личные данные
    name = State()
    surname = State()
    photo = State()

    # О компании
    about = State()
    status = State()
    mpy = State()
    industri = State()
    staf_count = State()
    field_activiti = State()

    # Оценка себя как специалиста
    otdel_prod = State()
    coll_center = State()
    production = State()
    marketplace = State()

    # Интерес к продукту
    interes = State()