# Generated by Django 2.2.4 on 2019-08-18 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PyAccountPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=80, verbose_name='Código')),
                ('name', models.CharField(max_length=80, verbose_name='Nombre')),
            ],
        ),
    ]
