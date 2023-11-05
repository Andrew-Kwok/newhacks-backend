# Generated by Django 4.2.7 on 2023-11-04 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='description',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='venue',
            name='image',
            field=models.ImageField(blank=True, upload_to='venue_images'),
        ),
        migrations.AddField(
            model_name='venue',
            name='indoor',
            field=models.BooleanField(blank=True, default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venue',
            name='suitable_for',
            field=models.CharField(default='', max_length=50),
        ),
    ]
