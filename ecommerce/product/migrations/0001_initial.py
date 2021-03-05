# Generated by Django 3.1.3 on 2021-03-05 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('hex_code', models.CharField(max_length=6, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('short_description', models.TextField()),
                ('full_description', models.TextField()),
                ('price', models.IntegerField()),
                ('availability', models.IntegerField()),
                ('size', models.CharField(max_length=16)),
                ('weight', models.IntegerField()),
                ('colors', models.ManyToManyField(to='product.Color')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.manufacturer')),
                ('similar_to', models.ManyToManyField(to='product.Product')),
            ],
        ),
    ]
