# Generated by Django 4.1.4 on 2022-12-15 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoe', '0005_remove_cart_table_brand_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_table',
            name='SHOES_ID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shoe.shoes_table'),
        ),
    ]
