# Generated by Django 2.2.4 on 2019-08-18 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0038_pyproduct_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('online', models.BooleanField(default=False, verbose_name='Online')),
            ],
        ),
    ]