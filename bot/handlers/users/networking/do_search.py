from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from fuzzywuzzy import fuzz

from loader import dp, bot
from sql import User, Feedback, DontShow
from keyboards.inline import search_kb, result_kb
from states import Tinder

from handlers.date_update import update_user_last_in


async def show(message: types.Message, state: FSMContext):
    update_user_last_in(message.from_user.id)
    await message.delete()
    data = await state.get_data()

    try:
        user = data['users'][data['page']]
        text = f"Имя: {user.name} \n" \
            f"Обо мне: \n\n{user.about}"

        fb = Feedback.select().where(Feedback.user == user.id)
        mark = 10

        marks = []

        for el in fb:
            marks.append(el.mark)

        for el in marks:
            mark += int(el)

        if len(marks):
            mark -= 10
            mark = mark/(len(marks))

        try:
            await bot.send_photo(
                chat_id=message.chat.id,
                photo=user.photo,
                caption=text,
                reply_markup=result_kb(mark)
            )
        except Exception as e:
            await message.answer(
                text=text,
                reply_markup=result_kb(mark)
            )

    except Exception as e:
        data = await state.get_data()
        data['page'] = 0
        await state.update_data(data)

        text = "Больше никого не нашлось( \n"
        text += "Попробуйте изменить параметры поиска \n"

        await message.answer(
            text=text,
            reply_markup=search_kb
        )


@dp.callback_query_handler(text='do_search', state=Tinder.started)
async def do_search(c: types.CallbackQuery, state: FSMContext):
    update_user_last_in(c.from_user.id)
    data = await state.get_data()
    users = User.select()
    ds = DontShow.select().where(DontShow.user_1 == c.from_user.id)

    users_list = []
    dont_show = []

    try:
        for el in ds:
            dont_show.append(el.user_1)
            dont_show.append(el.user_2)
    except:
        pass

    for user in users:
        dontsh = False
        for el in dont_show:
            if str(el) == str(user.tg_id):
                dontsh = True

        if dontsh == True:
            continue

        if str(c.from_user.id) != str(user.tg_id):
            is_exist = False

            if len(data['city']) > 0:
                a = fuzz.token_set_ratio(data['city'], user.about_1)
                if a > 35:
                    users_list.append(user)
                    is_exist = True
                    continue

            elif len(data['region']) > 0:
                a = fuzz.token_set_ratio(data['region'], user.about_2)
                if a > 35:
                    users_list.append(user)
                    is_exist = True
                    continue

            elif len(data['industri']) > 0:
                a = fuzz.token_set_ratio(data['industri'], user.about_3)
                if a > 35:
                    users_list.append(user)
                    is_exist = True
                    continue

            elif len(data['hobbi']) > 0:
                a = fuzz.token_set_ratio(data['hobbi'], user.about_4)
                if a > 35:
                    users_list.append(user)
                    is_exist = True
                    continue
            else:
                users_list.append(user)
                is_exist = True

    data['users'] = users_list
    data['page'] = 0
    await state.update_data(data)

    await show(c.message, state)


@dp.callback_query_handler(text='next', state=Tinder.started)
async def next(c: types.CallbackQuery, state: FSMContext):
    update_user_last_in(c.from_user.id)
    data = await state.get_data()
    data['page'] += 1
    await state.update_data(data)

    await show(c.message, state)


@dp.callback_query_handler(text='DontShow', state=Tinder.started)
async def next(c: types.CallbackQuery, state: FSMContext):
    update_user_last_in(c.from_user.id)
    data = await state.get_data()
    data['page'] += 1
    await state.update_data(data)

    ds = DontShow()
    ds.user_1 = c.from_user.id
    ds.user_2 = data['users'][data['page']].tg_id
    ds.save()

    await show(c.message, state)


@dp.callback_query_handler(text='back', state=Tinder.started)
async def back(c: types.CallbackQuery, state: FSMContext):
    update_user_last_in(c.from_user.id)
    data = await state.get_data()

    text = "Бизнес тиндер \n"
    text += f"Должность(-и): {data['profi']} \n" if len(data['profi']) != 0 else ''

    await c.message.answer(
        text=text,
        reply_markup=search_kb
    )