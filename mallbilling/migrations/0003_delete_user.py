# Generated by Django 4.2.1 on 2023-06-15 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mallbilling', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]