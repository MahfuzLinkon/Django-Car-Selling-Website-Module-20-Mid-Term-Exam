# Generated by Django 5.0.6 on 2024-06-17 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_alter_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]