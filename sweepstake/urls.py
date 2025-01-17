"""sweepstake URL Configuration

"""
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('raffles.urls')),
]
