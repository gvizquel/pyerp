# Generated by Django 2.2.4 on 2019-08-18 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0041_delete_baseuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseconfig',
            name='main_company_id',
            field=models.ForeignKey(blank=True, null=True, on_delete='cascade', to='base.PyCompany'),
        ),
    ]
