from ..bot.loader import dp, bot


def send_to_user(user_id, text):
    bot.send_message(user_id, text)