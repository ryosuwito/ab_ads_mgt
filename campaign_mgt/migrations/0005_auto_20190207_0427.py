# Generated by Django 2.1.5 on 2019-02-07 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_mgt', '0002_auto_20190207_0427'),
        ('agent_mgt', '0001_initial'),
        ('advertiser_mgt', '0001_initial'),
        ('area_db', '0001_initial'),
        ('campaign_mgt', '0004_auto_20190207_0411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='vehicle_models',
        ),
        migrations.AddField(
            model_name='campaign',
            name='advertiser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='advertiser_mgt.Advertiser'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='agen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='agent_mgt.Agent'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='timezone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='campaign',
            name='vehicle_brand',
            field=models.ManyToManyField(to='vehicle_mgt.VehicleBrand'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='vehicle_model',
            field=models.ManyToManyField(to='vehicle_mgt.VehicleModel'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='vehicle_type',
            field=models.ManyToManyField(to='vehicle_mgt.VehicleType'),
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='city',
        ),
        migrations.AddField(
            model_name='campaign',
            name='city',
            field=models.ManyToManyField(to='area_db.City'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='installation_address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='province',
        ),
        migrations.AddField(
            model_name='campaign',
            name='province',
            field=models.ManyToManyField(to='area_db.Province'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='status',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='terms_and_conditions',
            field=models.TextField(),
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='vehicle_color',
        ),
        migrations.AddField(
            model_name='campaign',
            name='vehicle_color',
            field=models.ManyToManyField(to='vehicle_mgt.VehicleColor'),
        ),
    ]
