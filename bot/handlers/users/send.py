from aiogram import types
import aiogram

from loader import dp, bot

from sql import User


@dp.message_handler(commands=['send'], state='*', commands_ignore_caption=False, content_types=types.ContentType.ANY)
async def bot_start(message: types.Message):
    """Рассылка приглашений в гильдии, чаты"""
    try:
        print("test" + str(message))
        if message.photo:
            print("aaa")
            param = message.caption.split(' ')
            print(param)
            if param[2] == "change_ph":
                user = User.get(User.tg_id == param[1])
                user.photo = message.photo[-1].file_id
            else:
                ph = message.photo[-1].file_id
                print(ph)
                # await bot.send_photo(  # does not work
                #     chat_id=param[1],
                #     photo=ph,
                #     caption=f'{message.text.replace(param[1], "").replace(param[0], "")}'
                # )
        else:
            param = message.text.split(' ')
            await bot.send_message(param[1], f'{message.text.replace(param[1], "").replace(param[0], "")}')
    except:
        pass
