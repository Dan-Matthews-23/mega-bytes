# Generated by Django 5.0.2 on 2024-03-18 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0004_alter_basket_basket_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='product_name',
            field=models.CharField(default='Test', editable=False, max_length=32),
        ),
    ]
