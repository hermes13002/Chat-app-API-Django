# Generated by Django 5.1.4 on 2024-12-30 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp_api_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='first_name null'),
        ),
    ]