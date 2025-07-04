# Generated by Django 5.2.3 on 2025-06-17 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tabla', models.CharField(max_length=20, verbose_name='Clase de Tipo')),
                ('codigo', models.CharField(max_length=10, verbose_name='Codigo')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Parametro',
                'verbose_name_plural': 'Parametros',
                'db_table': 'parametro',
                'constraints': [models.UniqueConstraint(fields=('nombre_tabla', 'codigo'), name='unique_nombre_tabla_codigo')],
            },
        ),
    ]
