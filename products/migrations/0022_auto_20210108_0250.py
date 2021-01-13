# Generated by Django 3.0.6 on 2021-01-07 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20210107_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='box_size',
            field=models.CharField(choices=[('50х50х35', '50х50х35'), ('60х60х40', '60х60х40'), ('60х60х40-P', '60х60х40-P'), ('80х80х40', '80х80х40'), ('80х80х40-P', '80х80х40-P'), ('240х185х120', '240х185х120'), ('270х220х70', '270х220х70')], default='80х80х40', max_length=20),
        ),
    ]
