# Generated by Django 2.1 on 2018-09-27 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0046_auto_20180927_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postponedpost',
            name='status',
            field=models.CharField(blank=True, choices=[('postponed', 'Отложен'), ('queue', 'В очереди'), ('process', 'Рассылается'), ('done', 'Разослан')], max_length=9, null=True, verbose_name='Статус'),
        ),
    ]
