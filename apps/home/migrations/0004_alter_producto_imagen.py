# Generated by Django 4.1.2 on 2022-11-16 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_producto_disponibilidad_producto_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.FileField(default=None, upload_to='static/img/productos'),
        ),
    ]