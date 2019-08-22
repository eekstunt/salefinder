# Generated by Django 2.1 on 2018-10-15 23:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0075_auto_20181015_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackdialogue',
            name='last_message_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 15, 23, 30, 25, 375407, tzinfo=utc), verbose_name='Время последнего сообщения (часовой пояс UTC)'),
        ),
    ]