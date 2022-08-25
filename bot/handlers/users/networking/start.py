from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.storage import FSMContext

from loader import dp
from keyboards.inline import search_kb
from states import Tinder
from sql import User


@dp.message_handler(Text(contains='Бизнес тиндер', ignore_case=True))
async def start(message: types.Message, state: FSMContext):
    user = User.get(User.tg_id == message.from_user.id)

    # Очистка reply клавиатуры
    _ck_ = await message.answer('<code>Clearing keyboard...</code>', reply_markup=ReplyKeyboardRemove())
    await _ck_.delete()

    await message.answer(
        text="Бизнес тиндер \n" \
            "Здесь вы можете найти людей и договориться о бизнес-встречи \n" \
            "Для поиска вы можете использовать фильтры",
        reply_markup=search_kb
    )

    data = {
        'profi': [],
        'industri': [],
        'city': [],
        'region': [],
        'hobbi': [],
        'page': 0
    }

    await Tinder.started.set()
    await state.update_data(data)


async def show(message: types.Message, state: FSMContext):
    data = await state.get_data()

    # Очистка reply клавиатуры
    _ck_ = await message.answer('<code>Clearing keyboard...</code>', reply_markup=ReplyKeyboardRemove())
    await _ck_.delete()

    text="Бизнес тиндер \n"
    text += f"Категория 1 (Личное): {data['city']} \n" if len(data['city']) > 0 else ''
    text += f"Категория 2 (Бизнес): {data['hobbi']} \n" if len(data['hobbi']) > 0 else ''
    text += f"Категория 3 (запросы): {data['region']} \n" if len(data['region']) > 0 else ''
    text += f"Категория 4 (Компетенции): {data['industri']} \n" if len(data['industri']) > 0 else ''

    await message.answer(
        text=text,
        reply_markup=search_kb
    )

    await Tinder.started.set()
