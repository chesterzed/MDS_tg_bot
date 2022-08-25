from peewee import *
from .BaseModel import BaseModel


class Feedback(BaseModel):
    """Отзывы на пользователей телегарм"""
    user = CharField(verbose_name='user', max_length=50)
    mark = CharField(verbose_name='mark', max_length=3)
    desc = CharField(verbose_name='desc', max_length=200, null=True)
    photo = CharField(verbose_name='photo', max_length=200, null=True)

    class Meta:
        table_name = 'work_feedbacks'


try:
    Feedback.create_table()
except:
    pass