# Generated by Django 3.2.7 on 2021-12-15 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0019_auto_20211215_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designations',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='designation_department', to='hrms.departments'),
        ),
        migrations.AlterField(
            model_name='designations',
            name='directorate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='designation_directorate', to='hrms.directorates'),
        ),
        migrations.AlterField(
            model_name='designations',
            name='division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='designation_division', to='hrms.divisions'),
        ),
        migrations.AlterField(
            model_name='designations',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='designation_section', to='hrms.sections'),
        ),
    ]
