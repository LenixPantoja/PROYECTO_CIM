# Generated by Django 4.2.6 on 2024-03-07 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppComputadoras', '0006_alter_accesorios_foto_acta_recepcion_accesorio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mouse',
            name='foto_acta_recepcion',
            field=models.ImageField(blank=True, null=True, upload_to='mouses/'),
        ),
        migrations.AlterField(
            model_name='mouse',
            name='foto_acta_salida',
            field=models.ImageField(blank=True, null=True, upload_to='mouses/'),
        ),
        migrations.AlterField(
            model_name='mouse',
            name='foto_factura',
            field=models.ImageField(blank=True, null=True, upload_to='mouses/'),
        ),
        migrations.AlterField(
            model_name='mouse',
            name='foto_requisicion_mouse',
            field=models.ImageField(blank=True, null=True, upload_to='mouses/'),
        ),
        migrations.AlterField(
            model_name='mouse',
            name='registro_fotografico_mouse',
            field=models.ImageField(blank=True, null=True, upload_to='mouses/'),
        ),
    ]