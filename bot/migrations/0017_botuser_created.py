# Generated by Django 2.1 on 2018-09-16 16:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0016_auto_20180915_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='botuser',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Первый запуск бота'),
            preserve_default=False,
        ),
    ]