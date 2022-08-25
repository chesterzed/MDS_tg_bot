from peewee import *
from .BaseModel import BaseModel


class User(BaseModel):
    """Пользователь телегарм"""
    # Личные данные
    phone = CharField(verbose_name='phone', max_length=50)
    tg_id = TextField(verbose_name='tg_id')
    name = CharField(verbose_name='name', max_length=50, null=True)
    photo = TextField(verbose_name='photo_id', null=True)

    # Информация для нетворкинга
    about = TextField()
    # Данные из админки
    # Категория 1
    about_1 = CharField(verbose_name='about_1', max_length=1000)

    # Категория 2
    about_2 = CharField(verbose_name='about_2', max_length=1000)

    # Категория 3
    about_3 = CharField(verbose_name='about_3', max_length=1000)

    # Категория 4
    about_4 = CharField(verbose_name='about_4', max_length=1000)

    # Чаты
    chat = CharField(verbose_name='chat', max_length=50)

    class Meta:
        table_name = 'work_users'


class DontShow(BaseModel):
    """Не показывать в нетворкинге"""
    user_1 = CharField(verbose_name='user_1', max_length=50)
    user_2 = CharField(verbose_name='user_2', max_length=50)

    class Meta:
        table_name = 'work_dont_show'


try:
    DontShow.drop_table()
    DontShow.create_table()
    User.create_table()
except:
    pass