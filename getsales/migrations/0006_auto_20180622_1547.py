# Generated by Django 2.0.6 on 2018-06-22 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getsales', '0005_auto_20180622_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='notes',
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
    ]