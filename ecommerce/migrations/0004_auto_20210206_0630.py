# Generated by Django 3.1.6 on 2021-02-06 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_auto_20210206_0508'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer_name',
            field=models.CharField(default='Dennis ivy', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.TextField(default='Jl. Jombang raya No. 56'),
        ),
    ]
