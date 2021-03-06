# Generated by Django 4.0.4 on 2022-04-30 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.SmallIntegerField(choices=[(0, 'Admin'), (1, 'Ordinary'), (2, 'Superuser')], default=1, verbose_name='Type')),
                ('phone_number', models.CharField(blank=True, max_length=13, null=True, unique=True, verbose_name='Phone Number')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True, verbose_name='Email')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last Name')),
                ('gender', models.SmallIntegerField(blank=True, choices=[(0, 'Male'), (1, 'Female')], default=1, null=True, verbose_name='Gender Type')),
                ('street', models.CharField(blank=True, max_length=255, null=True, verbose_name='Street')),
                ('house_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='House Number')),
                ('otp_key', models.CharField(blank=True, max_length=24, null=True, verbose_name='Otp Key')),
                ('time_otp', models.BigIntegerField(blank=True, null=True, verbose_name='Time Otp')),
                ('remember_me', models.BooleanField(default=False, verbose_name='Remember me')),
                ('status', models.SmallIntegerField(blank=True, choices=[(1, 'Active'), (0, 'Inactive'), (-1, 'Deleted')], null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
