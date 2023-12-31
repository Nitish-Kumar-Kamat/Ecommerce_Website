# Generated by Django 4.2.4 on 2023-09-12 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_delete_itemmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('order_id', models.CharField(max_length=100)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
    ]
