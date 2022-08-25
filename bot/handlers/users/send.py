from aiogram import types

from loader import dp, bot


@dp.message_handler(commands=['send'], state='*')
async def bot_start(message: types.Message):
    """Рассылка приглашений в гильдии, чаты"""
    try:
        param = message.text.split(' ')
        await bot.send_message(param[1], f'{message.text.replace(param[1], "").replace(param[0], "")}')

    except:
        pass