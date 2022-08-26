from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.storage import FSMContext

from loader import dp, bot
from states import Anketa
from sql import User
from keyboards.default import reg_kb, main_kb


@dp.message_handler(commands=['start'], state='*')
@dp.message_handler(Text(contains='главное меню', ignore_case=True), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    try:
        await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=main_kb)
        
    except Exception as e:
        await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=reg_kb)


@dp.callback_query_handler(text='main_menu', state='*')
async def main_menu(c: types.CallbackQuery, state: FSMContext):
    await c.message.answer("Главное меню", reply_markup=main_kb)
    await state.finish()

    
@dp.message_handler(Text(contains='Регистрация', ignore_case=True))
async def reg(message: types.Message):
    await Anketa.name.set()
    await message.answer(text="Для начала пользования ботом необходимо заполнить анкету\n " \
                        "Пришли свой номер телефона для этого нажми на кнопку \n" \
                        "Если кнопка не появилась, нажмите на иконку клавиатуры рядом с кнопкой отправить"   
                            , reply_markup=ReplyKeyboardMarkup(
                            [
                                [KeyboardButton("Отправить номер телефона", request_contact=True)]
                            ],
                            resize_keyboard=True
                        ))
