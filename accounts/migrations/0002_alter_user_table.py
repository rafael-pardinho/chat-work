# Generated by Django 5.1.3 on 2024-11-25 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]