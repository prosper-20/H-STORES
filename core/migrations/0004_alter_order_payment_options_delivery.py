# Generated by Django 4.1.4 on 2023-02-24 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_order_payment_amount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order_payment',
            options={'ordering': ['-date_created'], 'verbose_name': 'Ordered & Paid', 'verbose_name_plural': 'Ordered & Paid'},
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('L_G_A', models.CharField(max_length=100)),
                ('delivery_fee', models.DecimalField(decimal_places=2, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.order_payment')),
            ],
        ),
    ]
