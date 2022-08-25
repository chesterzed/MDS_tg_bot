from cgitb import text
from email import message
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.storage import FSMContext

from loader import dp, bot
from sql import User, Feedback
from keyboards.inline import search_kb, result_kb
from states import Tinder
from .do_search import show


@dp.callback_query_handler(text='feedback', state=Tinder.started)
async def feedback(c: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user = data['users'][data['page']]

    await c.message.answer("Поставте отметку от 1 до 10")
    await Tinder.feedback.set()
    data['user'] = user
    await state.update_data(data)


@dp.message_handler(state=Tinder.feedback)
async def mark(message: types.Message, state: FSMContext):
    try:
        if int(message.text) > 0 and int(message.text) <= 10:
            data = await state.get_data()
            user_id = data['user'].id

            fb = Feedback()
            fb.user = user_id
            fb.mark = message.text
            fb.desc = 'Без текста'
            fb.save()

            await message.answer('Напишите комментарий не более 200 символов')
            await Tinder.desc.set()
            data['fb'] = fb.id
            await state.update_data(data)
        
        else:
            await message.answer("Пришлите только цифру от 1 до 10")

    except:
        await message.answer("Пришлите только цифру от 1 до 10")


@dp.message_handler(state=Tinder.desc)
async def mark(message: types.Message, state: FSMContext):
    try:
        if len(message.text) < 200:
            data = await state.get_data()
            fb = Feedback.get(Feedback.id == data['fb'])
            fb.desc = message.text
            fb.save()

            await Tinder.started.set()
            await message.answer("Cпасибо за отзыв")
            await show(message=message, state=state)
        
        else:
            await message.answer("Пришлите комментарий не более 200 символов")

    except:
        await message.answer("Пришлите комментарий не более 200 символов")


@dp.callback_query_handler(text='view_feedback', state=Tinder.started)
async def view_feedback(c: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user = data['users'][data['page']].id
    feedbacks = Feedback.select().where(Feedback.user == user)

    for fb in feedbacks:
        await c.message.answer(
            f"Оценка - {fb.mark} \n\n" \
            f"{fb.desc}" 
        )

    await show(c.message, state)
