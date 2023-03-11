# Generated by Django 4.1.4 on 2023-03-11 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_product_specifications'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images')),
            ],
            options={
                'verbose_name_plural': 'Product Images',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='other_images',
            field=models.ManyToManyField(to='shop.myproductimages'),
        ),
    ]
