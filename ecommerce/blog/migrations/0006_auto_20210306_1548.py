# Generated by Django 3.1.3 on 2021-03-06 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210306_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created_on',
            new_name='created_at',
        ),
    ]