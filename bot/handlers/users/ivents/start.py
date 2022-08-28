from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text

from loader import dp, bot
from sql import Ivent, User

from handlers.date_update import update_user_last_in


@dp.message_handler(Text(contains='Мероприятия', ignore_case=True))
async def mychat(message: types.Message):
    update_user_last_in(message.from_user.id)
    user = User.get(User.tg_id == message.from_user.id)
    ivents = Ivent().select()

    await message.answer("Вот список мероприятий на этой неделе", reply_markup=ReplyKeyboardMarkup(
        [
            [KeyboardButton('Главное меню')]
        ],
        resize_keyboard=True
    ))
    for el in ivents:
        text = f'{el.name}\n' \
            f'{el.type_ivent}\n\n' \
            f'{el.desc}\n\n' \
            f'{el.date}'
        try:
            await bot.send_photo(
                chat_id=message.chat.id,
                photo=types.InputFile(str(el.photo).replace('//', '/').replace("""\\""", '/')),
                caption=text
            )
        except:
            await message.answer(text)