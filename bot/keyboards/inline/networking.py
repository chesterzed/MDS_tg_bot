from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


search_kb = InlineKeyboardMarkup(row_width=2)
do_search = InlineKeyboardButton(text='Найти', callback_data='do_search')
city = InlineKeyboardButton(text='Личное', callback_data='edit_city')
region = InlineKeyboardButton(text='Бизнес', callback_data='edit_region')
industri = InlineKeyboardButton(text='Запросы', callback_data='edit_industri')
hobbi = InlineKeyboardButton(text='Компетенции', callback_data='edit_hobbi')
main_menu = InlineKeyboardButton(text="Главное меню", callback_data="main_menu")
search_kb.add(do_search)
search_kb.add(city, hobbi, industri, region)
search_kb.add(main_menu)


def result_kb(mark):
    kb = InlineKeyboardMarkup(row_width=2)
    connect = InlineKeyboardButton(text='Связаться', callback_data='connect')
    ds = InlineKeyboardButton(text='Не показывать', callback_data='DontShow')
    feedback = InlineKeyboardButton(text='Оставить отзыв', callback_data='feedback')
    view_feedback = InlineKeyboardButton(text=f'Посмотреть отзывы (⭐{mark}/10)', callback_data='view_feedback')
    next = InlineKeyboardButton(text='Далее', callback_data='next')
    back = InlineKeyboardButton(text='Изменить или остановить поиск', callback_data='back')
    kb.add(connect, ds)
    kb.add(view_feedback)
    kb.add(feedback)
    kb.add(next)
    kb.add(back)
    return kb
