from rest_framework import serializers
from .models import Asset, Management, Device, Mold, JlType

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ('id', 'key', 'value')

class ManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = ('id', 'code', 'name', 'address', 'assistant_manager', 'outer_phone')

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'qrcode', 'code', 'name', 'asset_no', 'specs', 'arrival_date',
            'duty_officer', 'management_man', 'asset_class', 'use_status',
            'price', 'remark', 'created_at', 'updated_at')

class JlTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JlType
        fields = ('id', 'key', 'value')

class MoldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mold
        fields = ('id', 'qrcode', 'code', 'hole_count', 'specs', 'arrival_date',
            'duty_officer', 'management_man', 'asset_class', 'jl_type', 'jl_dosage',
            'use_status', 'location', 'price', 'remark', 'created_at', 'updated_at')
