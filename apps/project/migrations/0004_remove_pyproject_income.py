# Generated by Django 2.2.4 on 2019-08-17 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20190817_2158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pyproject',
            name='income',
        ),
    ]
