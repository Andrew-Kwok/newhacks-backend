""" venue/serializers.py
"""
from rest_framework import serializers

from .models import (
    Venue,
)


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'


class VenueListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = 'slug', 'name', 'description', 'image', 'address', 'web', 'rating', 'weather', 'category'
