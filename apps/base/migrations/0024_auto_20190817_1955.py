# Generated by Django 2.2.4 on 2019-08-17 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_auto_20190817_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pypartner',
            name='email',
            field=models.EmailField(blank=True, max_length=40, verbose_name='Correo'),
        ),
    ]
