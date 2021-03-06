# Generated by Django 2.1.5 on 2019-02-20 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_bankname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='bank_account_name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='bank_branch_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='bank_name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='on_behalf',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='bankname',
            name='bank_name',
            field=models.CharField(max_length=60),
        ),
    ]
