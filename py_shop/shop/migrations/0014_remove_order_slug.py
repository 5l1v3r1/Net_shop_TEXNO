# Generated by Django 2.2 on 2019-06-05 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_order_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='slug',
        ),
    ]