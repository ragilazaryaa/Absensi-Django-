# Generated by Django 4.2.4 on 2024-10-03 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_absen_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='karyawan',
            name='divisi',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
