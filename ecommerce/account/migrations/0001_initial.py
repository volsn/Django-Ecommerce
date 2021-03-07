# Generated by Django 3.1.3 on 2021-03-07 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(default='account/default.png', upload_to='account')),
                ('name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('full_address', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=64)),
                ('postal_code', models.CharField(max_length=32)),
                ('country', models.CharField(choices=[('US', 'United States'), ('CA', 'Canada'), ('UA', 'Ukraine')], max_length=2)),
                ('telephone', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]