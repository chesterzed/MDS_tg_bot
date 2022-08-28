from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.storage import FSMContext

from loader import dp
from states import Tinder
from sql import TaskConnect, User

from handlers.date_update import update_user_last_in


@dp.callback_query_handler(text='connect', state=Tinder.started)
async def connect(c: types.CallbackQuery, state: FSMContext):
    update_user_last_in(c.from_user.id)
    data = await state.get_data()
    user = data['users'][data['page']]
    await state.update_data({'user': user})

    await c.message.answer('Напишите почему вы хотите связаться с этим пользователем')
    await Tinder.connect.set()


@dp.message_handler(state=Tinder.connect)
async def about(message: types.Message, state:FSMContext):
    update_user_last_in(message.from_user.id)
    data = await state.get_data()
    user_from = User.get(User.tg_id == message.from_user.id)
    user_to = data['user']
    about = message.text

    task = TaskConnect()
    task.user_from = user_from.phone
    task.user_to = user_to.phone
    task.about = about
    task.save()

    await message.answer("Заявка успешно отправлена, скоро вам на неё ответят.", reply_markup=ReplyKeyboardMarkup(
        [
            [KeyboardButton('Главное меню')]
        ],
        resize_keyboard=True
    ))