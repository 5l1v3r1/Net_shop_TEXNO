# Generated by Django 2.2 on 2019-04-23 18:04

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import shop.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to=shop.models.image_folder)),
                ('priority', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('image', models.ImageField(blank=True, upload_to=shop.models.image_folder)),
                ('priority', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('image', models.ImageField(blank=True, upload_to=shop.models.image_folder)),
                ('priority', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to=shop.models.image_folder)),
                ('priority', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ThemeFront',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('image', models.ImageField(upload_to=shop.models.image_folder)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=120)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('image', models.ImageField(blank=True, upload_to=shop.models.image_folder)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('available', models.BooleanField(default=True, verbose_name='В наличии')),
                ('stock', models.PositiveIntegerField(verbose_name='На складе')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('priority', models.BooleanField(default=False)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
            ],
        ),
    ]
