# Generated by Django 5.0.2 on 2024-03-11 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0002_remove_basket_user_id_basket_default_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='order_number',
            field=models.CharField(editable=False, max_length=32),
        ),
    ]
