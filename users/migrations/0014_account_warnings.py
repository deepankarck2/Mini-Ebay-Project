# Generated by Django 4.1.2 on 2022-12-13 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_remove_account_rating_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='warnings',
            field=models.IntegerField(default=0),
        ),
    ]