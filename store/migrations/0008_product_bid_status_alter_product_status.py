# Generated by Django 4.1.2 on 2022-12-08 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_rename_bidding_price_product_bid_starting_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bid_status',
            field=models.BooleanField(default=False, help_text='0=Show, 1=Hidden'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=False, help_text='0=Show, 1=Hidden'),
        ),
    ]
