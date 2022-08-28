from aiogram import executor

import hook as h
import logging

from loader import dp, bot
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
import time
from sql.BaseModel import db


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)

async def on_startup_h(dp):
    await bot.set_webhook("109.68.213.180:443")
    # insert code here to run it after start


async def on_shutdown_h(dp):
    logging.warning('Shutting down..')

    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()

    # Close DB connection (if used)
    await dp.storage.close()
    await dp.storage.wait_closed()

    logging.warning('Bye!')


if __name__ == '__main__':
    # bot.delete_webhook()

    # Ставим заново вебхук
    # bot.set_webhook(url=h.WEBHOOK_URL_BASE + h.WEBHOOK_URL_PATH,
    #                 certificate=open(h.WEBHOOK_SSL_CERT, 'r'))

    # # Указываем настройки сервера CherryPy
    # cherrypy.config.update({
    #     'server.socket_host': h.WEBHOOK_LISTEN,
    #     'server.socket_port': h.WEBHOOK_PORT,
    #     'server.ssl_module': 'builtin',
    #     'server.ssl_certificate': h.WEBHOOK_SSL_CERT,
    #     'server.ssl_private_key': h.WEBHOOK_SSL_PRIV
    # })
    #
    # # Собственно, запуск!
    # cherrypy.quickstart(h.WebhookServer(), h.WEBHOOK_URL_PATH, {'/': {}})

    # executor.set_webhook(
    #     dispatcher=dp,
    #     webhook_path=h.WEBHOOK_URL_PATH,
    #     skip_updates=True,
    #     on_startup=on_startup_h,
    #     on_shutdown=on_shutdown_h,
    #     check_ip=False,
    # )

    executor.start_webhook(
        dispatcher=dp,
        webhook_path=h.WEBHOOK_URL_PATH,
        skip_updates=True,
        on_startup=on_startup_h,
        on_shutdown=on_shutdown_h,
        check_ip=False,
    )

    executor.start_polling(dp, on_startup=on_startup)

    while True:
        db.close()
        db.connect()
        time.sleep(9000)
