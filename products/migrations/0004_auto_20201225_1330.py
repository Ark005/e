# Generated by Django 3.1.4 on 2020-12-25 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20201225_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=None, null=True),
        ),
    ]
