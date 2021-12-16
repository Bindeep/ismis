# Generated by Django 3.2.7 on 2021-12-14 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0003_auto_20211213_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='nationality',
            field=models.CharField(choices=[('Uganda', 'Uganda'), ('Kenya', 'Kenya'), ('Rwanda', 'Rwanda'), ('South Sudan', 'South Sudan'), ('Burundi', 'Burundi'), ('Tanzania', 'Tanzania'), ('Non EAC Country', 'Non EAC Country')], default='Uganda', max_length=50),
        ),
        migrations.AlterField(
            model_name='employees',
            name='nin',
            field=models.CharField(default='12345678912345', max_length=14),
        ),
    ]
