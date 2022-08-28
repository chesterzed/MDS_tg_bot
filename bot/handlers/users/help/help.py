from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text

from loader import dp
from sql import User, TaskConnect
from keyboards.default import help_kb, back_kb
from states.Help import Help

from handlers.date_update import update_user_last_in


@dp.message_handler(Text(contains='помощь', ignore_case=True))
async def help_start(message: types.Message):
    update_user_last_in(message.from_user.id)
    await Help.start.set()
    await message.answer("Чем могу помочь?", reply_markup=help_kb)


@dp.message_handler(Text(contains='Как пользоваться ботом', ignore_case=True), state=Help.start)
async def use(message: types.Message):
    await message.answer("Как пользоваться ботом", reply_markup=back_kb)


@dp.message_handler(Text(contains='Сформировать индивидуальный запрос', ignore_case=True), state=Help.start)
async def answer(message: types.Message):
    await Help.oborot.set()
    await message.answer("Какой у вас оборот баланса", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=Help.oborot)
async def oborot(message: types.Message):
    await Help.desc.set()
    await message.answer("Опишите ваш запрос текстом не более чем 200 символов")


@dp.message_handler(state=Help.desc)
async def desc(message: types.Message):
    if len(message.text) <= 200:
        user_from = User.get(User.tg_id == message.from_user.id)
        task = TaskConnect()
        task.user_from = user_from.phone
        task.user_to = 0
        task.about = str(message.text)
        if message.photo:
            task.about = str(message.caption)
        task.save()

        await message.answer("Ваш запрос отправлен!\nСкоро с вами свяжутся")
        await help_start(message)
    else:
        await message.answer("Ваш запрос превышает максимальную длину 200 символов. Опишите проблему короче")



@dp.message_handler(Text(contains='Назад', ignore_case=True), state=Help.start)
async def back(message: types.Message):
    await Help.start.set()
    await message.answer("Чем могу помочь?", reply_markup=help_kb)