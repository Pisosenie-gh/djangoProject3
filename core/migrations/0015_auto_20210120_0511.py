# Generated by Django 3.1.5 on 2021-01-20 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20210120_0444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='name_kz',
            new_name='name_kk',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='text_kz',
            new_name='text_kk',
        ),
    ]
