from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


reg_kb = ReplyKeyboardMarkup(
    [
        [KeyboardButton("О нас")],
        [KeyboardButton("Партнерская программа")],
        [KeyboardButton("Регистрация")],
    ],
    resize_keyboard=True
)


main_kb = ReplyKeyboardMarkup(
    [
        [KeyboardButton("База знаний"), KeyboardButton("Новости МДС")],
        [KeyboardButton("Бизнес тиндер"), KeyboardButton("Мой профиль")],
        [KeyboardButton("Мой чат")],
        [KeyboardButton("О нас"), KeyboardButton("Помощь")],
        [KeyboardButton("Мероприятия")],
        # [KeyboardButton("Срочная помощь"), KeyboardButton("Единый портал делового собрания")],
        [KeyboardButton("Архив встреч")],
    ],
    resize_keyboard=True
)