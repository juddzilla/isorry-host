# Generated by Django 5.0.1 on 2024-01-05 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apology', '0002_auto_20240105_0350'),
    ]

    operations = [
        migrations.RenameField('apology', 'user_id', 'user'),
    ]
