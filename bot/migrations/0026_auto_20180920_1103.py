# Generated by Django 2.1 on 2018-09-20 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0025_auto_20180920_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='base',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
