# Generated by Django 4.0.4 on 2022-05-12 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_producto_fecha_ingreso_remove_producto_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ManyToManyField(related_name='categorias', to='app.categoriaproducto'),
        ),
    ]