# Generated by Django 4.2 on 2023-04-20 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0010_merge_20230419_2002'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together=set(),
        ),
    ]
