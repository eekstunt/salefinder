# Generated by Django 2.1 on 2018-10-10 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0066_botuser_feedback_enabled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackdialogue',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dialogue', to='bot.BotUser', verbose_name='Пользователь'),
        ),
    ]
