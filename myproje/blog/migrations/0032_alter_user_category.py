# Generated by Django 4.1 on 2022-09-20 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_alter_user_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='category',
            field=models.ManyToManyField(to='blog.category'),
        ),
    ]