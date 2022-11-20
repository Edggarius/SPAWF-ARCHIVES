# Generated by Django 4.1.2 on 2022-11-20 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_merge_20221120_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='category',
            field=models.CharField(choices=[('', ''), ('Robótica', 'Robótica'), ('Herramientas', 'Herramientas'), ('Cables, accesorios e insumos', 'Cables, accesorios e insumos')], default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.PositiveIntegerField(),
        ),
    ]
