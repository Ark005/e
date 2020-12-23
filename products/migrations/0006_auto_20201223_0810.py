# Generated by Django 3.1.3 on 2020-12-23 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20201223_0656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='tirazh',
        ),
        migrations.AddField(
            model_name='friend',
            name='first_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friend',
            name='last_name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friend',
            name='likes',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friend',
            name='lives_in',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]