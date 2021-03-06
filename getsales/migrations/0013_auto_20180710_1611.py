# Generated by Django 2.0.6 on 2018-07-10 22:11

from django.db import migrations, models
import getsales.validators


class Migration(migrations.Migration):

    dependencies = [
        ('getsales', '0012_auto_20180710_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='cash_sales',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='notes',
            field=models.CharField(blank=True, max_length=240, validators=[getsales.validators.validate_decimal]),
        ),
    ]
