# Generated by Django 4.2.14 on 2024-08-04 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0008_fdapplication_account_rdapplication_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fdapplication',
            name='account',
        ),
        migrations.RemoveField(
            model_name='rdapplication',
            name='account',
        ),
    ]
