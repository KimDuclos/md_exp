# Generated by Django 2.2.3 on 2019-08-01 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0002_auto_20190730_2308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='current_location',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='updated_at',
        ),
    ]