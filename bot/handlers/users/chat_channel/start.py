from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text

from loader import dp
from sql import Chat, Channel, User

from handlers.date_update import update_user_last_in


@dp.message_handler(Text(contains='Мой чат', ignore_case=True))
async def mychat(message: types.Message):
    # update_user_last_in(message.from_user.id)
    try:
        user = User.get(User.tg_id == message.from_user.id)
        chat = Chat.get(Chat.id == user.chat)

        await message.answer(
            text="Вот ваш чат. Вы можете в нем общаться",
            reply_markup=InlineKeyboardMarkup(row_width=1).add(
                InlineKeyboardButton(text='Перейти в чат', url=chat.link)
            )
        )

    except:
        await message.answer("Вы пока что не распределены в чат, ожидайте. Мы вам обязательно сообщим когда для вас будет создан чат")


@dp.message_handler(Text(contains='Новости МДС', ignore_case=True))
async def news(message: types.Message):
    # update_user_last_in(message.from_user.id)
    user = User.get(User.tg_id == message.from_user.id)
    try:
        news = Channel.select()
        text = 'Вот список новостных каналов \n'

        if len(news) > 0:
            for el in news:
                text += f'{el.name} - @{el.link} \n'

            await message.answer(text)
        else:
            await message.answer("Новостных каналов пока не создали. Мы вам обязательно сообщим когда создадим их.")

    except:
        await message.answer("Новостных каналов пока не создали. Мы вам обязательно сообщим когда создадим их.")