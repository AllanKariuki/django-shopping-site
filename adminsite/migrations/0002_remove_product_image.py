# Generated by Django 4.1.7 on 2023-04-12 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminsite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
