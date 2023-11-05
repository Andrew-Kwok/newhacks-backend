""" venue/models.py
"""
import random
import string

from django.db import models


def upload_path(instance, filename):
    slug = instance.slug
    random_chars = ''.join(random.choice(string.ascii_lowercase) for _ in range(4))
    file_extension = filename.split('.')[-1]
    filename = f'{slug}-{random_chars}.{file_extension}'
    return f'venue_images/{filename}'


# Create your models here.
class Venue(models.Model):
    CATEGORY_CHOICES = (
        ('indoor', 'Indoor'),
        ('outdoor', 'Outdoor'),
        ('hybrid', 'Hybrid'),
    )

    # General
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=50, unique=True)
    image = models.ImageField(upload_to=upload_path)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=500, default='')
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    web = models.URLField(blank=True)
    email_address = models.EmailField(blank=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    suitable_for = models.CharField(max_length=50)

    # Statistics
    rating = models.FloatField()
    capacity = models.IntegerField()
    parking = models.IntegerField()
    traffic = models.IntegerField()
    scenery = models.FloatField()
    comment = models.TextField(blank=True)

    # Weather
    weather = models.IntegerField()

    def __str__(self):
        return f'{self.name} [{self.rating}]'

    class Meta:
        verbose_name_plural = 'Venues'
        ordering = ['name']
