# Generated by Django 4.1.4 on 2022-12-23 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xlease', '0004_alter_item_leased_to_alter_item_owned_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='lease_period',
            field=models.IntegerField(blank=True, help_text='Leased period in Number of days'),
        ),
    ]