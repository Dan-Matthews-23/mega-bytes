# Generated by Django 5.0.2 on 2024-04-14 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0018_reviews_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='product',
        ),
    ]
