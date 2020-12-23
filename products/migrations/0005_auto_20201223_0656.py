# Generated by Django 3.1.3 on 2020-12-23 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20201222_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='first_name',
        ),
        migrations.AddField(
            model_name='friend',
            name='nick_name',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]