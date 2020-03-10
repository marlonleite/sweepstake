from django.urls import path

from .views import RaffleApiView

urlpatterns = [
    path('', RaffleApiView.as_view(), name="raffle"),
]
