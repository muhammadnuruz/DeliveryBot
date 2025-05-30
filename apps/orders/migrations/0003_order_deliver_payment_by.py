# Generated by Django 5.0.1 on 2025-03-30 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_delivery_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='deliver_payment_by',
            field=models.CharField(choices=[('user', 'Paid by User'), ('customer', 'Paid by customer')], default='user', help_text='Who will pay the delivery price', max_length=10),
        ),
    ]
