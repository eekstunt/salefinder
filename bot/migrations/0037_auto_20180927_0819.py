# Generated by Django 2.1 on 2018-09-27 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0036_auto_20180926_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postponedpost',
            name='type',
            field=models.CharField(choices=[('post', 'Пост'), ('offer', 'Оффер')], max_length=5, verbose_name='Тип публикации'),
        ),
    ]
