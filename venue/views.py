""" venue/views.py
"""
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Venue, VenueSurvey
from .serializers import VenueListSerializer, VenueSerializer, VenueSurveySerializer


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
        venue_data = serializer.data

        venue_surveys = VenueSurvey.objects.filter(venue=venue)
        venue_data['venue_surveys'] = VenueSurveySerializer(venue_surveys, many=True).data

        return Response(venue_data)


class VenueList(APIView):
    def get(self, request):
        venues = Venue.objects.all()
        serializer = VenueListSerializer(venues, many=True)
        return Response(serializer.data)


class VenueSurveyAPIView(APIView):
    def post(self, request, slug):
        venue = Venue.objects.get(slug=slug)
        if not venue:
            return Response(
                {'error': 'Venue not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        venue_survey = VenueSurvey(
            venue=venue,
            rating=request.data['rating'],
            traffic=request.data['traffic'],
            scenery=request.data['scenery'],
            comment=request.data['comment'],
        )
        venue_survey.save()

        return Response({'success': 'Survey submitted.'})
