# Generated by Django 2.1 on 2018-10-10 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0065_feedbackdialogue_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='botuser',
            name='feedback_enabled',
            field=models.BooleanField(default=False),
        ),
    ]