from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.parsers import JSONParser
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from cars.models import Car
from cars.serializers import CarSerializer


class CarList(generics.ListCreateAPIView):

    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDetails(generics.RetrieveUpdateDestroyAPIView):

    queryset = Car.objects.all()
    serializer_class = CarSerializer



