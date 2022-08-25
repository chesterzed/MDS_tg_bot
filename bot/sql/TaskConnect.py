from peewee import *
from .BaseModel import BaseModel


class TaskConnect(BaseModel):
    """Таск по связыванию пользователей через нетворкинг"""
    user_from = CharField(max_length=100)
    user_to = CharField(max_length=100)
    about = TextField()
    photo_path = TextField()

    class Meta:
        table_name = 'work_taskconnect'
