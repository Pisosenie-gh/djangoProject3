# Generated by Django 3.1.5 on 2021-02-18 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20210217_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='document',
            field=models.FileField(default=None, upload_to='documents/'),
        ),
    ]
