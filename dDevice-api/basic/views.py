#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters
from .models import Supplier, Organization
from .serializers import (SupplierSerializer, OrganizationSerializer)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class SupplierFilter(filters.FilterSet):
    code = filters.CharFilter(name='code', lookup_expr='icontains')
    name = filters.CharFilter(name='name', lookup_expr='icontains')

    class Meta:
        model = Supplier
        fields = ['code', 'name']

class SupplierViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    pagination_class = StandardResultsSetPagination
    filter_class = SupplierFilter

class OrganizationFilter(filters.FilterSet):
    code = filters.CharFilter(name='code', lookup_expr='icontains')
    name = filters.CharFilter(name='name', lookup_expr='icontains')

    class Meta:
        model = Organization
        fields = ['code', 'name']

class OrganizationViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    pagination_class = StandardResultsSetPagination
    filter_class = OrganizationFilter
