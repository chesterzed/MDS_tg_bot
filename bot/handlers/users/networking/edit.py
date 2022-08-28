from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.storage import FSMContext

from loader import dp
from states import Tinder
from .start import show

from handlers.date_update import update_user_last_in


@dp.callback_query_handler(text='edit_city', state=Tinder.started)
async def city(c: CallbackQuery, state:FSMContext):
    update_user_last_in(c.from_user.id)
    await c.message.answer("Пришлите описание личных качеств")
    await Tinder.city.set()


@dp.message_handler(state=Tinder.city)
async def edit_city(message: Message, state: FSMContext):
    update_user_last_in(message.from_user.id)
    data = await state.get_data()
    data['city'] = message.text
    await state.update_data(data)

    await show(message=message, state=state)


@dp.callback_query_handler(text='edit_hobbi', state=Tinder.started)
async def hobbi(c: CallbackQuery, state:FSMContext):
    update_user_last_in(c.from_user.id)
    await c.message.answer("Пришлите описание компании")
    await Tinder.hobbi.set()


@dp.message_handler(state=Tinder.hobbi)
async def edit_hobbi(message: Message, state: FSMContext):
    update_user_last_in(message.from_user.id)
    data = await state.get_data()
    data['hobbi'] = message.text
    await state.update_data(data)

    await show(message=message, state=state)   


@dp.callback_query_handler(text='edit_region', state=Tinder.started)
async def region(c: CallbackQuery, state:FSMContext):
    update_user_last_in(c.from_user.id)
    await c.message.answer("Пришлите запросов (куда направлено внимание)")
    await Tinder.region.set()


@dp.message_handler(state=Tinder.region)
async def edit_region(message: Message, state: FSMContext):
    update_user_last_in(message.from_user.id)
    data = await state.get_data()
    data['region'] = message.text
    await state.update_data(data)

    await show(message=message, state=state)   


@dp.callback_query_handler(text='edit_industri', state=Tinder.started)
async def industri(c: CallbackQuery, state:FSMContext):
    update_user_last_in(c.from_user.id)
    await c.message.answer("Пришлите описание навыков(скиллов)")
    await Tinder.industri.set()


@dp.message_handler(state=Tinder.industri)
async def edit_industri(message: Message, state: FSMContext):
    update_user_last_in(message.from_user.id)
    data = await state.get_data()
    data['industri'] = message.text
    await state.update_data(data)

    await show(message=message, state=state)   
