# Generated by Django 3.1.3 on 2021-03-06 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210306_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='selected',
            field=models.BooleanField(default=False),
        ),
    ]
