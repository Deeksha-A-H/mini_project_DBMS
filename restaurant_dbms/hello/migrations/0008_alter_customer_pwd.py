# Generated by Django 4.0.1 on 2022-02-07 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_rename_contact_no_customer_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='pwd',
            field=models.CharField(max_length=8),
        ),
    ]
