# Generated by Django 3.1.3 on 2021-01-13 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20210113_0818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billingaddress',
            old_name='city',
            new_name='cellular',
        ),
    ]
