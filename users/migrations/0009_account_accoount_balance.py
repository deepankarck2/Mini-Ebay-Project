# Generated by Django 4.1.2 on 2022-12-12 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_userblacklist'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='accoount_balance',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
