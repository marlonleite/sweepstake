from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RaffleSerializer


class RaffleApiView(APIView):
    """
        RaffleApiView Sort Items.
    """

    @method_decorator(cache_page(60 * 60 * 2))
    def post(self, request, format=None):
        serializer = RaffleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
