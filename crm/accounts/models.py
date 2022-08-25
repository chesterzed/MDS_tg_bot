from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.TextField(verbose_name='name', null=True)
    phone = models.TextField(verbose_name='phone', null=True)

    manage = models.BooleanField(verbose_name='manage personel', null=True)
    user_manage = models.BooleanField(verbose_name='manage user', null=True)
    channel_manage = models.BooleanField(verbose_name='manage channel', null=True)
    chat_manage = models.BooleanField(verbose_name='manage chat', null=True)
    # content_manage = models.BooleanField(verbose_name='manage content')

    class Meta:
        managed=True
        verbose_name = 'User'
        verbose_name_plural = 'Users'
