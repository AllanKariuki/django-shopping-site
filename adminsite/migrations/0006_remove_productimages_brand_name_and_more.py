# Generated by Django 4.1.7 on 2023-04-12 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientsite', '0002_remove_orderitem_order_remove_orderitem_product_and_more'),
        ('adminsite', '0005_productimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimages',
            name='brand_name',
        ),
        migrations.RemoveField(
            model_name='productimages',
            name='category_name',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductImages',
        ),
    ]
