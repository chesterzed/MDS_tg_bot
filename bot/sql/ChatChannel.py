from .BaseModel import BaseModel
from peewee import *


class Channel(BaseModel):
    """Модель каналов"""
    name = CharField(verbose_name='Название канала', max_length=50)
    link = CharField(verbose_name='Ссылка', max_length=100)
    desc = TextField(verbose_name='Описание')
    tg_id = CharField(verbose_name='tg_id', max_length=50)

    class Meta:
        table_name='work_channel'


class Chat(BaseModel):
    """Модель гильдий"""
    tg_id = CharField(verbose_name='tg_id', max_length=50) 
    name = CharField(verbose_name='Название чата', max_length=50)
    link = CharField(verbose_name='link', max_length=50)

    class Meta:
        table_name = 'work_chat'

    
try:
    Chat.create_table()

except:
    pass