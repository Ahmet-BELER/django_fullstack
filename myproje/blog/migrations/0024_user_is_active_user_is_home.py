# Generated by Django 4.1 on 2022-09-20 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_remove_user_is_active_remove_user_is_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_home',
            field=models.BooleanField(default=False),
        ),
    ]
