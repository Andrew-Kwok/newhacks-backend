# Generated by Django 4.2.7 on 2023-11-05 00:10

from django.db import migrations, models
import venue.models


class Migration(migrations.Migration):

    dependencies = [
        ('venue', '0002_venue_description_venue_image_venue_indoor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='image',
            field=models.ImageField(blank=True, upload_to=venue.models.upload_path),
        ),
    ]