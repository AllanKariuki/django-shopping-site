# Generated by Django 4.1.7 on 2023-04-12 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientsite', '0005_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
