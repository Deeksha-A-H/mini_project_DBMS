# Generated by Django 4.0.1 on 2022-03-17 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0020_alter_orders_cuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='cuid',
        ),
    ]
