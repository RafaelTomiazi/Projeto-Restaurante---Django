# Generated by Django 5.0.6 on 2024-06-25 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_reservation_date_alter_reservation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.CharField(max_length=20),
        ),
    ]
