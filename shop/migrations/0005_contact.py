# Generated by Django 4.1.4 on 2023-03-10 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_supersubcategory_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
