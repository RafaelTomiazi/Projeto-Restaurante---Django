# Generated by Django 5.0.6 on 2024-06-20 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_reservation_remove_myprofile_user_delete_servico_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
