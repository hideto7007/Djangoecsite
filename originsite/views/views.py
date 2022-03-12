from django.shortcuts import render, get_object_or_404
from rest_framework import status, views, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action
from rest_framework import viewsets, filters
from django.http import JsonResponse
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


from originsite.model.models import SampleData
from originsite.serializer.serializers import SampleDataSerializer


class SampleDataListCreateAPIView(viewsets.ModelViewSet):
    queryset = SampleData.objects.all()
    serializer_class = SampleDataSerializer




