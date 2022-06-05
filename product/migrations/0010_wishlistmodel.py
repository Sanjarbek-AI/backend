# Generated by Django 4.0.4 on 2022-06-05 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_storemodel_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishlistModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(blank=True, null=True, verbose_name='Product id')),
                ('user_id', models.IntegerField(blank=True, null=True, verbose_name='User id')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Wishlist',
                'verbose_name_plural': 'Wishlists',
            },
        ),
    ]
