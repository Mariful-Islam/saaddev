from django.shortcuts import render

from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from django.apps import apps
from django.contrib import admin 
from django.contrib.admin.sites import AlreadyRegistered 


from base.models import *
from saad_dev_api.serializers import *
from django.conf import settings

import json


# Create your views here.


class SaadDevTables(APIView):
    
    def get(self, *args, **kwargs):
        tables = apps.all_models['base']
        data = []
        for key in tables:
            data.append(key)
        return Response(data=data)
    

class Services(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    parser_classes = [MultiPartParser, FormParser]


class Service(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    parser_classes = [MultiPartParser, FormParser]


class Projects(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    parser_classes = [MultiPartParser, FormParser]


class Project(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    parser_classes = [MultiPartParser, FormParser]


# class Services(ListCreateAPIView):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer
#     parser_classes = [MultiPartParser, FormParser]


# class Service(RetrieveUpdateDestroyAPIView):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer
#     parser_classes = [MultiPartParser, FormParser]
    


class EcomTables(APIView):

    def get(self, *args, **kwargs):
        tables = apps.all_models['ecom']
        data = []
        for key in tables:
            data.append(key)
        return Response(data=data)

    