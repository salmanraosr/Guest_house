# Generated by Django 4.1.7 on 2023-10-16 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gkapp', '0002_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='checkin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='checkout',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_available', models.BooleanField(default=False)),
                ('room_no', models.CharField(max_length=100)),
                ('room_desc', models.CharField(max_length=100)),
                ('room_capacity', models.IntegerField()),
                ('GuestHouses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gkapp.guesthouses')),
                ('RoomCategories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gkapp.roomcategories')),
            ],
            options={
                'db_table': 'rooms',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin', models.DateField(blank=True, null=True)),
                ('checkout', models.DateField(blank=True, null=True)),
                ('no_of_days', models.IntegerField()),
                ('total_amount', models.FloatField()),
                ('GuestHouses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gkapp.guesthouses')),
                ('RoomCategories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gkapp.roomcategories')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gkapp.customer')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gkapp.employee')),
                ('room_rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gkapp.roomrates')),
                ('rooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gkapp.rooms')),
            ],
            options={
                'db_table': 'reservation',
            },
        ),
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('approval_date', models.DateTimeField(auto_now=True)),
                ('approved_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gkapp.employee')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gkapp.request')),
            ],
            options={
                'db_table': 'approval',
            },
        ),
    ]
