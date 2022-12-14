# Generated by Django 4.1.2 on 2022-12-13 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_account_account_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='average_rating',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='rating_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='rating_total',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
