# Generated by Django 2.1 on 2018-10-10 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0064_feedbackdialogue'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackdialogue',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bot.BotUser', verbose_name='Пользователь'),
            preserve_default=False,
        ),
    ]