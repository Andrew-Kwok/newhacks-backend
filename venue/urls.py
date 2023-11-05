""" venue/urls.py
"""
from django.urls import path

from .views import (
    VenueList,
    VenueDetail,
)

urlpatterns = [
    path('', VenueList.as_view()),
    path('<str:slug>/', VenueDetail.as_view()),
]
