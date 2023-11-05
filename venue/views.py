""" venue/views.py
"""
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Venue
from .serializers import VenueListSerializer, VenueSerializer


# Create your views here.
class VenueDetail(APIView):
    def get(self, request, slug):
        venue = Venue.objects.get(slug=slug)
        if not venue:
            return Response(
                {'error': 'Venue not found.'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = VenueSerializer(venue)
        return Response(serializer.data)


class VenueList(APIView):
    def get(self, request):
        venues = Venue.objects.all()
        serializer = VenueListSerializer(venues, many=True)
        return Response(serializer.data)
