# Generated by Django 3.1.3 on 2021-01-04 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210104_0803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='pt',
            field=models.DateField(blank=True, null=True),
        ),
    ]