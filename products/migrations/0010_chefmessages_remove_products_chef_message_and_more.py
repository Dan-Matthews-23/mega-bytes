# Generated by Django 5.0.2 on 2024-04-21 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_products_calorie_content_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChefMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chef_message', models.TextField(default='')),
            ],
        ),
        migrations.RemoveField(
            model_name='products',
            name='chef_message',
        ),
        migrations.AlterField(
            model_name='products',
            name='calorie_content',
            field=models.IntegerField(default=1),
        ),
    ]
