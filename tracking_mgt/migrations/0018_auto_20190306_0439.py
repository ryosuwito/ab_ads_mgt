# Generated by Django 2.1.5 on 2019-03-06 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking_mgt', '0017_blacklist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpsdailyreport',
            name='mileage',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=9),
        ),
    ]