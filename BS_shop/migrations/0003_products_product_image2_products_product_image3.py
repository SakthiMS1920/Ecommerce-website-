# Generated by Django 4.2.4 on 2023-12-29 08:26

import BS_shop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BS_shop', '0002_products_product_image1'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_image2',
            field=models.ImageField(blank=True, null=True, upload_to=BS_shop.models.getFileName),
        ),
        migrations.AddField(
            model_name='products',
            name='product_image3',
            field=models.ImageField(blank=True, null=True, upload_to=BS_shop.models.getFileName),
        ),
    ]
