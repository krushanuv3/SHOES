# Generated by Django 4.1.4 on 2022-12-08 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CONTACT_TABLE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MESSAGE', models.CharField(max_length=300)),
                ('EMAIL_ID', models.EmailField(max_length=254)),
                ('PHONE_NO', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='STOCK_TABLE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('COMMENT', models.CharField(max_length=300)),
                ('BRAND_ID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shoe.brand_table')),
                ('CATEGORY_ID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shoe.category_table')),
                ('SHOES_ID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shoe.shoes_table')),
            ],
        ),
        migrations.CreateModel(
            name='ORDER_TABLE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ORDER_TYPE', models.CharField(max_length=300)),
                ('ORDER_NAME', models.CharField(max_length=300)),
                ('COUNT', models.IntegerField()),
                ('BRAND_ID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shoe.brand_table')),
                ('L_ID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shoe.login_table')),
                ('SHOES_ID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shoe.shoes_table')),
            ],
        ),
        migrations.CreateModel(
            name='FEEDBACK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RATINGS', models.CharField(max_length=300)),
                ('COMMENT', models.CharField(max_length=300)),
                ('L_ID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shoe.login_table')),
            ],
        ),
        migrations.CreateModel(
            name='CART_TABLE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SHOES_NAME', models.CharField(max_length=300)),
                ('DATE', models.DateTimeField()),
                ('QUANTITY', models.IntegerField()),
                ('BRAND_ID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shoe.brand_table')),
                ('CATEGORY_ID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shoe.category_table')),
                ('L_ID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shoe.login_table')),
                ('SHOES_ID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shoe.shoes_table')),
            ],
        ),
    ]