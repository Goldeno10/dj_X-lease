# Generated by Django 4.1.4 on 2022-12-24 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xlease', '0009_customer_profile_image_item_slug_itemimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemimage',
            old_name='item_id',
            new_name='item',
        ),
    ]
