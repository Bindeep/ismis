# Generated by Django 3.2.7 on 2021-12-14 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0004_auto_20211214_0912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addresses',
            old_name='addressable_type',
            new_name='addressable_type',
        ),
    ]
