# Generated by Django 5.0.6 on 2024-06-17 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
