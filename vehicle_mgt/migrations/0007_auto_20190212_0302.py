# Generated by Django 2.1.5 on 2019-02-12 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_mgt', '0006_auto_20190208_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_brand',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_model',
            field=models.CharField(default='', max_length=255),
        ),
    ]
