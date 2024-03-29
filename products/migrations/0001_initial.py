# Generated by Django 3.2.23 on 2024-02-09 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=254)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('product_short_description', models.CharField(max_length=254)),
                ('product_long_description', models.TextField(verbose_name=1024)),
                ('product_image_url', models.URLField(verbose_name=1024)),
                ('product_rating', models.URLField(verbose_name=1024)),
                ('category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
            ],
        ),
    ]
