from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp

from handlers.date_update import update_user_last_in


@dp.message_handler(Text(contains='О нас', ignore_case=True))
async def reg(message: types.Message):
    update_user_last_in(message.from_user.id)
    await message.answer('О нас')


@dp.message_handler(Text(contains='Партнерская программа', ignore_case=True))
async def reg(message: types.Message):
    update_user_last_in(message.from_user.id)
    await message.answer('Партнерская программа')


@dp.message_handler(Text(contains='База знаний', ignore_case=True))
async def reg(message: types.Message):
    update_user_last_in(message.from_user.id)
    await message.answer('База знаний')


@dp.message_handler(Text(contains='Чат-гильдия', ignore_case=True))
async def reg(message: types.Message):
    update_user_last_in(message.from_user.id)
    await message.answer('гильдия')


@dp.message_handler(Text(contains='VIP чат', ignore_case=True))
async def reg(message: types.Message):
    update_user_last_in(message.from_user.id)
    await message.answer('VIP чат')


@dp.message_handler(Text(contains='Срочная помощь', ignore_case=True))
async def reg(message: types.Message):
    update_user_last_in(message.from_user.id)
    await message.answer('Срочная помощь')


@dp.message_handler(Text(contains='Единый портал делового собрания', ignore_case=True))
async def reg(message: types.Message):
    update_user_last_in(message.from_user.id)
    await message.answer('Единый портал делового собрания')


@dp.message_handler(Text(contains='Антикризисные меры', ignore_case=True))
async def reg(message: types.Message):
    update_user_last_in(message.from_user.id)
    await message.answer('Антикризисные меры')