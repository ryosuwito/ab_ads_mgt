# Generated by Django 2.1.5 on 2019-02-07 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_mgt', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiclemodel',
            name='vehicle_brand',
        ),
        migrations.RemoveField(
            model_name='vehiclemodel',
            name='vehicle_type',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicle_mgt.VehicleBrand'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicle_mgt.VehicleType'),
        ),
    ]
