# Generated by Django 4.2 on 2023-04-19 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_rename_product_cart_food'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='session_id',
            field=models.CharField(default='', max_length=32),
        ),
    ]
