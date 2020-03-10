"""sweepstake URL Configuration

"""
from django.urls import path, include

urlpatterns = [
    path('api/', include('raffles.urls')),
]
