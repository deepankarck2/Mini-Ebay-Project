# Generated by Django 4.1.2 on 2022-11-26 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_account_address_alter_account_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='warnings',
            field=models.IntegerField(default=0),
        ),
    ]
