# Generated by Django 2.0.6 on 2018-06-22 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getsales', '0003_sales_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='notes',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]
