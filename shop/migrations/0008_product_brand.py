# Generated by Django 4.1.4 on 2023-03-12 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_myproductimages_product_other_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='Adidas', max_length=150),
            preserve_default=False,
        ),
    ]
