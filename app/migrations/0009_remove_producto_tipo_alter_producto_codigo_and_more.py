# Generated by Django 4.0.4 on 2022-05-12 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_producto_categoria_producto_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='tipo',
        ),
        migrations.AlterField(
            model_name='producto',
            name='codigo',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='TipoProducto',
        ),
    ]