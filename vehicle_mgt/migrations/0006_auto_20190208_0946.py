# Generated by Django 2.1.5 on 2019-02-08 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_mgt', '0005_auto_20190208_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclebrand',
            name='vehicle_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicle_mgt.VehicleType'),
        ),
        migrations.AddField(
            model_name='vehiclemodel',
            name='vehicle_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicle_mgt.VehicleType'),
        ),
    ]
