# Generated by Django 3.2.23 on 2024-02-10 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_products_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category_id',
            field=models.IntegerField(default=0),
        ),
    ]
