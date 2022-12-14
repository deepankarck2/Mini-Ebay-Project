# Generated by Django 4.1.2 on 2022-11-19 20:16

from django.db import migrations, models
import django.db.models.deletion
import store.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to=store.models.get_file_path_cat)),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0=Default, 1=Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0=Default, 1=Hidden')),
                ('meta_title', models.CharField(max_length=150)),
                ('meta_keywords', models.CharField(max_length=150)),
                ('meta_description', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=50)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to=store.models.get_file_path_pro)),
                ('small_description', models.TextField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('original_price', models.FloatField()),
                ('bidding_price', models.FloatField()),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0=Default, 1=Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0=Default, 1=Hidden')),
                ('tag', models.CharField(max_length=150)),
                ('meta_title', models.CharField(max_length=150)),
                ('meta_keywords', models.CharField(max_length=150)),
                ('meta_description', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
    ]
