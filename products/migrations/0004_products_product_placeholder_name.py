# Generated by Django 3.2.23 on 2024-02-10 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_products_product_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_placeholder_name',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
