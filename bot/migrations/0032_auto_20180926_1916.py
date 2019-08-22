# Generated by Django 2.1 on 2018-09-26 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0031_auto_20180926_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postponedpost',
            name='image_place',
            field=models.CharField(choices=[('top', 'Сверху'), ('bottom', 'Снизу')], default='top', max_length=6, verbose_name='Расположение изображения'),
        ),
        migrations.AlterField(
            model_name='postponedpost',
            name='text',
            field=models.TextField(choices=[('fsdfsdfsdfsd\nfsdfsdf\\sdfsdf\nfdsfsdfdsf', 'fsdfsdfsdfsd\nfsdfsdf\\sdfsdf\nfdsfsdfdsf'), ('fsdfssdfsdfsd\nfsdfsdf\\sdfsdf\nfdsfsdfdsf', 'fsdfsdfsdfsd\nfsdfsdf\\sdfsdf\nfdsfsdfdsfags')], max_length=200, verbose_name='Текст (форматированный)'),
        ),
    ]