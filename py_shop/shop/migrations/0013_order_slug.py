# Generated by Django 2.2 on 2019-06-05 15:39

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20190605_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, populate_from='uvapisg4bh'),
            preserve_default=False,
        ),
    ]
