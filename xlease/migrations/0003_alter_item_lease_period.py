# Generated by Django 4.1.4 on 2022-12-23 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xlease', '0002_rename_zipode_city_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='lease_period',
            field=models.DurationField(blank=True),
        ),
    ]
