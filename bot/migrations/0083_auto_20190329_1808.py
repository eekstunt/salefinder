# Generated by Django 2.1.7 on 2019-03-29 18:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0082_auto_20181016_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackdialogue',
            name='last_message_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 29, 18, 8, 34, 676864, tzinfo=utc), verbose_name='Время последнего сообщения (часовой пояс UTC)'),
        ),
    ]