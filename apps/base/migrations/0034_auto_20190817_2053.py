# Generated by Django 2.2.4 on 2019-08-17 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_pyproduct_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pyproduct',
            name='type',
            field=models.CharField(choices=[('product', 'Almacenable'), ('consu', 'Consumible'), ('service', 'Servicio')], default='consu', max_length=64),
        ),
    ]
