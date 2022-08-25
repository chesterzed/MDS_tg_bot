from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup

from loader import dp, bot
from sql import User, TaskConnect
from keyboards.inline import profile_kb, edit_kb
from states.Profile import AnketaProfile


@dp.message_handler(Text(contains='Мой профиль', ignore_case=True))
@dp.message_handler(text='Назад к профилю', state='*')
async def start(message: types.Message):
    try:
        user = User.get(User.tg_id == message.from_user.id)
        text = f"Имя: {user.name} \n" \
            f"Обо мне: \n\n{user.about}"

        try:
            # Очистка reply клавиатуры
            _ck_ = await message.answer('<code>Clearing keyboard...</code>', reply_markup=ReplyKeyboardRemove())
            await _ck_.delete()

            await bot.send_photo(
                chat_id=message.from_user.id,
                photo=user.photo,
                caption=text,
                reply_markup=profile_kb
            )
        except Exception as e:
            await message.answer(text, reply_markup=profile_kb)

        await AnketaProfile.started.set()
    except:
        pass


@dp.callback_query_handler(text='edit', state=AnketaProfile.started)
async def edit(c: types.CallbackQuery):    
    # Очистка reply клавиатуры
    await c.message.answer('Редактирование профиля', reply_markup=ReplyKeyboardMarkup(
        [
            [KeyboardButton('Назад к профилю')]
        ],
        resize_keyboard=True
    ))
    await c.message.answer("Пришлите что вы хотите изменить, наш менеджер поменяет информацию. "
                           "Если нужно изменить фото пришлите фото")


@dp.message_handler(state=AnketaProfile.started)
@dp.message_handler(content_types=['photo'], state=AnketaProfile.started)
async def edit(message: types.Message):
    user_from = User.get(User.tg_id == message.from_user.id)
    about = message.text

    task = TaskConnect()
    task.user_from = user_from.phone
    task.user_to = 0
    task.about = str(about)

    if message.photo:
        task.about = str(message.caption)
        f_path = str(message.photo[-1].file_id)
        task.photo_path = f_path

    task.save()

    await message.answer("Наш менеджер поменяет информацию, ожидайте.")
    await start(message)
