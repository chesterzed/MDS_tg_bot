from aiogram.dispatcher.filters.state import State, StatesGroup


class AnketaProfile(StatesGroup):
    started = State()
    name = State()
    photo = State()
    city = State()
    family = State()
    mpy = State()
    industri = State()
    staf_count = State()
    admire = State()
    hobbi = State()
    name_company = State()
    site = State()
    region = State()
    role = State()
