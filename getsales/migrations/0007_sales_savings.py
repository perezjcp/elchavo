# Generated by Django 2.0.6 on 2018-06-27 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getsales', '0006_auto_20180622_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='savings',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
            preserve_default=False,
        ),
    ]
