# Generated by Django 5.0.3 on 2024-03-22 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_alter_client_phone_alter_lawyer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
