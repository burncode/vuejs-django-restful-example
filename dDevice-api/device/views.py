#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters
from .models import Asset, Management, Device, Mold, JlType
from .serializers import (AssetSerializer, ManagementSerializer, DeviceSerializer,
                        MoldSerializer, JlTypeSerializer)

class AssetViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    serializer_class = AssetSerializer
    queryset = Asset.objects.all()

class ManagementViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    serializer_class = ManagementSerializer
    
    def get_queryset(self):
        return Management.objects

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class DeviceFilter(filters.FilterSet):
    qrcode = filters.CharFilter(name='qrcode', lookup_expr='icontains')
    name = filters.CharFilter(name='name', lookup_expr='icontains')
    code = filters.CharFilter(name='code', lookup_expr='icontains')

    class Meta:
        model = Device
        fields = ['qrcode', 'name', 'code']

class DeviceViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()
    pagination_class = StandardResultsSetPagination
    filter_class = DeviceFilter

class JlTypeViewSet(ModelViewSet):
    serializer_class = JlTypeSerializer
    queryset = JlType.objects.all()
    
class MoldFilter(filters.FilterSet):
    qrcode = filters.CharFilter(name='qrcode', lookup_expr='icontains')
    code = filters.CharFilter(name='code', lookup_expr='icontains')

    class Meta:
        model = Mold
        fields = ['qrcode', 'code']

class MoldViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    serializer_class = MoldSerializer
    queryset = Mold.objects.all()
    pagination_class = StandardResultsSetPagination
    filter_class = MoldFilter
    