# Generated by Django 4.1.4 on 2022-12-15 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoe', '0006_cart_table_shoes_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_table',
            name='BRAND_ID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shoe.brand_table'),
        ),
    ]