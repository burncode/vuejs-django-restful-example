from rest_framework import serializers
from .models import Supplier, Organization

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('id', 'code', 'name', 'phone', 'address', 'remark')

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = fields = ('id', 'code', 'name', 'phone', 'address',
            'manager', 'remark')
