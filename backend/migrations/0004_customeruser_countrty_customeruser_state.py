# Generated by Django 4.2.14 on 2024-08-03 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_customeruser_avartar'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeruser',
            name='countrty',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='customeruser',
            name='state',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
