# Generated by Django 3.2.23 on 2024-02-10 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20240209_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (4, '5')], default=1),
        ),
    ]
