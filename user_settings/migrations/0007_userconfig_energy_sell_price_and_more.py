# Generated by Django 4.1 on 2022-09-14 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_settings', '0006_rename_energy_price_userconfig_energy_buy_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='userconfig',
            name='energy_sell_price',
            field=models.FloatField(default=0.2, verbose_name='Selling price for 1kWh (PLN)'),
        ),
        migrations.AlterField(
            model_name='userconfig',
            name='energy_buy_price',
            field=models.FloatField(default=0.8, verbose_name='Buying price for 1kWh (PLN)'),
        ),
    ]
