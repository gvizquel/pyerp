# Generated by Django 2.2.4 on 2019-08-20 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_websiteconfig'),
    ]

    operations = [
        migrations.AddField(
            model_name='websiteconfig',
            name='under_construction',
            field=models.BooleanField(default=False, verbose_name='En Construcción'),
        ),
    ]
