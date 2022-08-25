from aiogram import executor

import hook as h
import cherrypy

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


if __name__ == '__main__':
    bot.delete_webhook()

    # Ставим заново вебхук
    bot.set_webhook(url=h.WEBHOOK_URL_BASE + h.WEBHOOK_URL_PATH,
                    certificate=open(h.WEBHOOK_SSL_CERT, 'r'))

    # Указываем настройки сервера CherryPy
    cherrypy.config.update({
        'server.socket_host': h.WEBHOOK_LISTEN,
        'server.socket_port': h.WEBHOOK_PORT,
        'server.ssl_module': 'builtin',
        'server.ssl_certificate': h.WEBHOOK_SSL_CERT,
        'server.ssl_private_key': h.WEBHOOK_SSL_PRIV
    })

    # Собственно, запуск!
    cherrypy.quickstart(h.WebhookServer(), h.WEBHOOK_URL_PATH, {'/': {}})

    executor.start_polling(dp, on_startup=on_startup)
    
    while True:
        db.close()
        db.connect()
        time.sleep(18000)
