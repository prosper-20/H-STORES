# Generated by Django 4.1.4 on 2023-03-15 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bestseller',
            field=models.BooleanField(default=False),
        ),
    ]
