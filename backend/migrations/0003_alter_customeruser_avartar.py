# Generated by Django 4.2.14 on 2024-08-03 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_customeruser_avartar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='avartar',
            field=models.ImageField(blank=True, upload_to='avatars/'),
        ),
    ]
