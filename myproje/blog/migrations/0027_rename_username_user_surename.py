# Generated by Django 4.1 on 2022-09-20 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_alter_user_is_active_alter_user_is_home'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='surename',
        ),
    ]
