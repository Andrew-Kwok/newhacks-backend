""" venue/serializers.py
"""
from rest_framework import serializers

from .models import (
    Venue,
    VenueSurvey,
)


class VenueSurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = VenueSurvey
        fields = '__all__'


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'


class VenueListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = 'slug', 'name', 'description', 'image', 'address', 'web', 'rating', 'weather', 'category'
