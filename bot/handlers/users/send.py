from aiogram import types

from loader import dp, bot


@dp.message_handler(commands=['send'], state='*')
async def bot_start(message: types.Message):
    """Рассылка приглашений в гильдии, чаты"""
    try:
        if message.photo:
            param = message.caption.split(' ')
            ph = message.photo[-1].file_id
            await bot.send_photo(
                chat_id=param[1],
                photo=ph,
                caption=f'{message.text.replace(param[1], "").replace(param[0], "")}'
            )
        else:
            param = message.text.split(' ')
            await bot.send_message(param[1], f'{message.text.replace(param[1], "").replace(param[0], "")}')

    except:
        pass