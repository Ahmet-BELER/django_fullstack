# Generated by Django 4.1 on 2022-09-20 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_rename_surename_user_surname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_home',
            field=models.BooleanField(default=True),
        ),
    ]