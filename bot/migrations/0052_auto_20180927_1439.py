# Generated by Django 2.1 on 2018-09-27 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0051_auto_20180927_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postponedpost',
            name='offer_sizes',
            field=models.CharField(default='0 0.5', max_length=1024, verbose_name='Размеры EU (через пробел, с шагом 0.5)'),
        ),
    ]
