# Generated by Django 5.0.2 on 2024-04-28 11:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=254)),
                ('display_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChefMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chef_message', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_placeholder_name', models.CharField(max_length=254, null=True)),
                ('product_name', models.CharField(max_length=254)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('product_short_description', models.CharField(max_length=254)),
                ('protein_source', models.BooleanField(blank=True, null=True)),
                ('fibre_source', models.BooleanField(blank=True, null=True)),
                ('product_image_url', models.URLField(verbose_name=1024)),
                ('category_id', models.IntegerField(default=0)),
                ('calorie_content', models.IntegerField(default=1)),
                ('protein_content', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fibre_content', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fat_content', models.DecimalField(decimal_places=2, max_digits=6)),
                ('saturated_fat_content', models.DecimalField(decimal_places=2, max_digits=6)),
                ('carbohydrate_content', models.DecimalField(decimal_places=2, max_digits=6)),
                ('carbohydrate_sugar_content', models.DecimalField(decimal_places=2, max_digits=6)),
                ('salt_content', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='accounts.userprofile')),
                ('favourite_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='products.products')),
            ],
        ),
    ]
