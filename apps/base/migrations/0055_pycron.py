# Generated by Django 2.2.4 on 2019-08-21 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0054_auto_20190821_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='PyCron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Nombre')),
                ('active', models.BooleanField(default=False, verbose_name='Activo')),
                ('interval_type', models.CharField(choices=[('minutes', 'Almacenable'), ('hours', 'Horas'), ('work_day', 'Días laborales'), ('weeks', 'Semanas'), ('month', 'Meses')], default='hours', max_length=64)),
                ('model_name', models.CharField(max_length=40, verbose_name='Nombre')),
                ('function', models.CharField(max_length=40, verbose_name='Método')),
                ('number_call', models.IntegerField(default=-1, verbose_name='Precio')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
