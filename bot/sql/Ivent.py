from .BaseModel import BaseModel
from peewee import *


class Ivent(BaseModel):
    """Мероприятия"""
    name = CharField(max_length=255)
    type_ivent = CharField(max_length=255)
    date = CharField(max_length=255)
    desc = TextField()
    photo = TextField()

    class Meta:
        table_name = 'work_ivent'