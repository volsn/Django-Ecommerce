# Generated by Django 3.1.3 on 2021-03-06 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_review_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='updated_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
