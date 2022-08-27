import time
from datetime import date


# описать классы можно здесь (используются ниже)


def user_leave_checker():
    print("start checking...")
    while True:
        # users = User_tg.objects.all()     #  Здесь требуются классы user, task для добавления в БД
                                            #  Подключение к БД

        today = date.today()

        # for us in users:                  #  цикл где надо перебрать всех пользователей,
        #     dat = us.last_in              #  вычесть из их последнеднего захода в сеть today, и сравнить с 3-мя днями
                                            #  Если меньше то создать таск и отправить его в БД


        time.sleep(86400)                   #  Ожидание 24 часа


