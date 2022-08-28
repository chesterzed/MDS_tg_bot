from aiogram import types
from aiogram.types import InputFile
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.storage import FSMContext

from loader import dp, bot
from states import Anketa
from sql import User
from keyboards.default import main_kb


@dp.message_handler(content_types=['contact'], state=Anketa.name)
async def phone(message: types.Message, state: FSMContext):
    ph = str(message.contact['phone_number']).replace('+', '')
    print(message.chat.id)
    print(message.from_user.id)
    print(ph)

    try:
        print("suc")
        user = User.get(User.phone == ph)
        user.tg_id = message.from_user.id
        user.save()
        print("suc1")
        try:
            photo = await bot.send_photo(
                chat_id=message.from_user.id,
                photo=InputFile("/root/club2/bot/" + str(user.photo).replace('//', '/').replace("\\", '/'))
            )

            print("suc2")
            print(photo)
            user.photo = photo['photo'][0]['file_id']
            user.save()
            print("suc3")
        except:
            pass

        await message.answer('Вы успешно прошли регистрацию!', reply_markup=main_kb)
        print("suc4")
        await state.finish()
        print("suc5")

    
    except Exception as e:
        # print(e)
        await message.answer('Вас нет в базе, обратитесь к администритору')
