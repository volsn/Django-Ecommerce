# Generated by Django 3.1.3 on 2021-03-06 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210306_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]