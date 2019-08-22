# Generated by Django 2.1 on 2018-09-26 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0030_auto_20180920_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='postponedpost',
            name='image_place',
            field=models.CharField(choices=[('top', 'Сверху'), ('bottom', 'Снизу')], default='top', max_length=6, verbose_name=''),
        ),
        migrations.AddField(
            model_name='postponedpost',
            name='status',
            field=models.CharField(blank=True, choices=[('postponed', 'Отложена'), ('queue', 'В очереди'), ('process', 'Рассылается'), ('done', 'Разослана')], max_length=9, null=True, verbose_name='Статус'),
        ),
    ]