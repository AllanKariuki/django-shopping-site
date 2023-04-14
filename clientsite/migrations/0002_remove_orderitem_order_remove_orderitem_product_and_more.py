# Generated by Django 4.1.7 on 2023-04-12 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientsite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='requestforquotation',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='requestforservice',
            name='customer_name',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
        migrations.DeleteModel(
            name='RequestForQuotation',
        ),
        migrations.DeleteModel(
            name='RequestForService',
        ),
    ]
