from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


profile_kb = InlineKeyboardMarkup(row_width=1)
profile_kb.add(
    # InlineKeyboardButton('Скопировать приветствие', callback_data='copy'),
    InlineKeyboardButton('Редактировать профиль', callback_data='edit'),
    InlineKeyboardButton('Главное меню', callback_data='main_menu')
)

edit_kb = InlineKeyboardMarkup(row_width=1)
edit_kb.add(
    InlineKeyboardButton("Фото", callback_data='edit_photo'),
    InlineKeyboardButton("Имя", callback_data='edit_name'),
    InlineKeyboardButton("Личное", callback_data='edit_city'),
    InlineKeyboardButton("Бизнес", callback_data='edit_family'),
    InlineKeyboardButton("Запросы", callback_data='edit_admire'),
    InlineKeyboardButton("Компетенции", callback_data='edit_hobbi')
    # InlineKeyboardButton("Название компании", callback_data='edit_name_company'),
    # InlineKeyboardButton("Сайт", callback_data='edit_site'),
    # InlineKeyboardButton("Направление деятельности", callback_data='edit_industri'),
    # InlineKeyboardButton("Регион", callback_data='edit_region'),
    # InlineKeyboardButton("Годовой оборот", callback_data='edit_mpy'),
    # InlineKeyboardButton("Количество сотрудников", callback_data='edit_staf_count'),
    # InlineKeyboardButton("Должность", callback_data='edit_profi'),
)