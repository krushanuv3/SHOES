# Generated by Django 4.1.4 on 2022-12-17 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoe', '0013_remove_cart_table_cart_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order_table',
            old_name='ORDER_NAME',
            new_name='ADDRESS',
        ),
        migrations.RemoveField(
            model_name='order_table',
            name='BRAND_ID',
        ),
        migrations.RemoveField(
            model_name='order_table',
            name='COUNT',
        ),
        migrations.RemoveField(
            model_name='order_table',
            name='ORDER_TYPE',
        ),
        migrations.RemoveField(
            model_name='order_table',
            name='SHOES_ID',
        ),
        migrations.AddField(
            model_name='cart_table',
            name='ORDER_ID',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart_table',
            name='ORDER_STATUS',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order_table',
            name='DATETIME',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='order_table',
            name='ORDER_STATUS',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order_table',
            name='PAYMENT_STATUS',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order_table',
            name='TOTAL_AMOUNT',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shoe.cart_table'),
        ),
    ]
