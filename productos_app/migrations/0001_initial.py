# Generated by Django 5.1.2 on 2024-11-27 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('ID_producto', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Calorias', models.PositiveBigIntegerField()),
                ('Vitaminas', models.CharField(max_length=20)),
                ('Precio', models.PositiveBigIntegerField()),
                ('Stock', models.PositiveBigIntegerField()),
                ('ID_Proveedor', models.PositiveBigIntegerField()),
            ],
        ),
    ]
