from django.db import models


class Channel(models.Model):
    """Модель каналов"""
    name = models.CharField(verbose_name='Название канала', max_length=50)
    link = models.CharField(verbose_name='Ссылка', max_length=100)
    desc = models.TextField(verbose_name='Описание')
    tg_id = models.CharField(verbose_name='tg_id', max_length=50)

    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'


class Chat(models.Model):
    """Модель гильдий"""
    tg_id = models.CharField(verbose_name='tg_id', max_length=50)
    name = models.CharField(verbose_name='Название чата', max_length=50)
    link = models.CharField(verbose_name='link', max_length=50)

    class Meta:
        verbose_name = 'Гильдия'
        verbose_name_plural = 'Гильдии'


class User_tg(models.Model):
    """Пользователь телегарм"""
    # Личные данные
    phone = models.CharField(verbose_name='phone', max_length=50)
    tg_id = models.TextField(verbose_name='tg_id')
    name = models.CharField(verbose_name='name', max_length=50, null=True)
    photo = models.TextField(verbose_name='photo_id', null=True)

    # # Информация для нетворкинга
    about = models.TextField(verbose_name='about')
    # Данные из админки
    # Категория 1
    city = models.CharField(verbose_name='city', max_length=100)

    about_1 = models.TextField(verbose_name='about_1')

    # Категория 2
    about_2 = models.TextField(verbose_name='about_2')

    # Категория 3
    about_3 = models.TextField(verbose_name='about_3')

    # Категория 4
    about_4 = models.TextField(verbose_name='about_4')

    # Чаты
    chat = models.CharField(verbose_name='chat', max_length=50)

    class Meta:
        db_table = 'work_users'
        verbose_name = 'Пользователь тг'
        verbose_name_plural = 'Пользователи тг'


class DontShow(models.Model):
    """Не показывать в нетворкинге (для телеграма)"""
    user_1 = models.CharField(verbose_name='user_1', max_length=50)
    user_2 = models.CharField(verbose_name='user_2', max_length=50)

    class Meta:
        verbose_name = "Не показывать в нетворкинге (для телеграма)"
        verbose_name_plural = "Не показывать в нетворкинге (для телеграма)"


class Ivent(models.Model):
    """Мероприятия"""
    name = models.CharField(max_length=255)
    type_ivent = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    desc = models.TextField()
    photo = models.TextField()

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"


class Mailing(models.Model):
    """Рассылки"""
    name = models.CharField(max_length=255)
    desc = models.TextField()
    photo = models.TextField(verbose_name='photo_id', null=True)

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"


class TaskConnect(models.Model):
    """Таск по связыванию пользователей через нетворкинг"""
    user_from = models.CharField(max_length=100)
    user_to = models.CharField(max_length=100)
    about = models.TextField()
    photo_path = models.TextField()

    class Meta:
        verbose_name = "Таск"
        verbose_name_plural = "Таски"
