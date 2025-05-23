# Generated by Django 5.1.7 on 2025-05-08 08:59

import booking.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0017_remove_photogallery_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profiles', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg']), booking.models.validate_image_size]),
        ),
        migrations.AlterField(
            model_name='photogallery',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='gallery', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg']), booking.models.validate_image_size]),
        ),
        migrations.AlterField(
            model_name='touristspot',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='spots', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg']), booking.models.validate_image_size]),
        ),
    ]
