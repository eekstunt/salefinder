# Generated by Django 2.1 on 2018-10-11 18:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0071_auto_20181011_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackdialogue',
            name='ignored',
            field=models.BooleanField(default=False, verbose_name='Игнор'),
        ),
        migrations.AlterField(
            model_name='feedbackdialogue',
            name='last_message_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 11, 18, 36, 32, 758600, tzinfo=utc), verbose_name='Время последнего сообщения (часовой пояс UTC)'),
        ),
        migrations.AlterField(
            model_name='feedbackdialogue',
            name='status',
            field=models.CharField(choices=[('open', 'Открыт'), ('closed', 'Закрыт')], default='open', max_length=7, verbose_name='Статус'),
        ),
    ]
