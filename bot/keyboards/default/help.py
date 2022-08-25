from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


help_kb = ReplyKeyboardMarkup(
    [
        [KeyboardButton("Как пользоваться ботом")],
        [KeyboardButton("Сформировать индивидуальный запрос")],
        [KeyboardButton("Главное меню")],
    ],
    resize_keyboard=True
)


back_kb = ReplyKeyboardMarkup(
    [
        [KeyboardButton("Назад")],
    ],
    resize_keyboard=True
)