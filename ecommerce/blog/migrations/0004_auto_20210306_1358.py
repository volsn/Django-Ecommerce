# Generated by Django 3.1.3 on 2021-03-06 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210306_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='main_image',
            field=models.ImageField(blank=True, default='default.png', upload_to='blog'),
        ),
    ]
