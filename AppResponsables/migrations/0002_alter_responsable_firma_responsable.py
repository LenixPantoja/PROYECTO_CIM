# Generated by Django 4.2.6 on 2023-11-09 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppResponsables', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsable',
            name='firma_responsable',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]