# Generated by Django 4.1.4 on 2023-03-10 16:11

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_lga_delivery_prices'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='delivery_prices',
            options={'verbose_name_plural': 'Delivery Prices'},
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_fee',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='name', chained_model_field='city', default=1000, on_delete=django.db.models.deletion.CASCADE, to='orders.delivery_prices'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.lga'),
        ),
    ]