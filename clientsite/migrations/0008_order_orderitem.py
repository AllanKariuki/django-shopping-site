# Generated by Django 4.1.7 on 2023-04-12 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminsite', '0007_product'),
        ('clientsite', '0007_remove_order_customer_remove_orderitem_order_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('total_cost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=60)),
                ('phone', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254)),
                ('additional_information', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientsite.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminsite.product')),
            ],
        ),
    ]
