# Generated by Django 3.1.3 on 2021-01-13 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20191008_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingaddress',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='billingaddress',
            name='landmark',
            field=models.CharField(max_length=300),
        ),
    ]
