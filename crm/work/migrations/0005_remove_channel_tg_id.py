# Generated by Django 3.2.8 on 2022-06-16 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0004_channel_tg_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='tg_id',
        ),
    ]
