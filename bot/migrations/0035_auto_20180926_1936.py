# Generated by Django 2.1 on 2018-09-26 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0034_auto_20180926_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draft',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]