# Generated by Django 3.1.3 on 2020-12-22 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20201222_0743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='likes',
        ),
        migrations.AddField(
            model_name='friend',
            name='tirazh',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
