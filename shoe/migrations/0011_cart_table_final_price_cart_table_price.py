# Generated by Django 4.1.4 on 2022-12-16 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoe', '0010_delete_new_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_table',
            name='FINAL_PRICE',
            field=models.IntegerField(default=160),
        ),
        migrations.AddField(
            model_name='cart_table',
            name='PRICE',
            field=models.IntegerField(default=100),
        ),
    ]
