# Generated by Django 5.1.2 on 2024-11-28 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('ID_proveedor', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('Telefono', models.PositiveBigIntegerField()),
                ('Correo', models.CharField(max_length=50)),
                ('Empresa', models.CharField(max_length=50)),
                ('Productos', models.CharField(max_length=500)),
                ('Stock', models.PositiveBigIntegerField()),
                ('Rfc', models.CharField(max_length=20)),
            ],
        ),
    ]
