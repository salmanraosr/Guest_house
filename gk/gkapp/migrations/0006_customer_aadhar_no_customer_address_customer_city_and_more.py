# Generated by Django 4.1.7 on 2023-11-06 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gkapp', '0005_reservation_guest_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='aadhar_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='mobile_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
