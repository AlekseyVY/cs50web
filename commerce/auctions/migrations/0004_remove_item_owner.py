# Generated by Django 3.1.3 on 2020-12-09 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20201209_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='owner',
        ),
    ]