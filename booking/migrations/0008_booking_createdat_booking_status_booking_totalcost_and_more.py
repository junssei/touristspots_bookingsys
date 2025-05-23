# Generated by Django 5.1.7 on 2025-05-04 15:15

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_booking_bookingline_customuser_is_tourguide_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='createdAt',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='pending', max_length=20),
        ),
        migrations.AddField(
            model_name='booking',
            name='totalcost',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookingline',
            name='booking',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='booking.booking'),
        ),
        migrations.AddField(
            model_name='bookingline',
            name='numberOfPeople',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='bookingline',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
        migrations.AddField(
            model_name='bookingline',
            name='spot',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='booking.touristspot'),
        ),
        migrations.AddField(
            model_name='bookingline',
            name='visitDate',
            field=models.DateField(default='2025-10-10'),
        ),
        migrations.AddField(
            model_name='photogallery',
            name='caption',
            field=models.TextField(default='Enter your caption'),
        ),
        migrations.AddField(
            model_name='photogallery',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='touristspot',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profiles'),
        ),
        migrations.AlterField(
            model_name='photogallery',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='touristspot',
            name='openingday',
            field=models.CharField(default='00:00:00', max_length=15),
        ),
    ]
