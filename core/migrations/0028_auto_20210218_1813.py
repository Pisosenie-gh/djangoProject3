# Generated by Django 3.1.5 on 2021-02-18 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20210218_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='document',
            field=models.FileField(default=None, upload_to='docs/'),
        ),
    ]
