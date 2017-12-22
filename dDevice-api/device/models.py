# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# 管理单位
class Management(models.Model):
    code = models.CharField(max_length=50, help_text='编码')
    name = models.CharField(max_length=50, help_text='名称')
    address = models.CharField(max_length=200, help_text='所在地')
    assistant_manager = models.CharField(max_length=50, help_text='责任人')
    outer_phone = models.CharField(max_length=50, help_text='联系电话')

    def __str__(self):
        return self.code + ': ' + self.name

# 资产类别
class Asset(models.Model):
    key = models.CharField(max_length=200, help_text='键名')
    value = models.CharField(max_length=200, help_text='键名')

    def __str__(self):
        return self.key + ': ' + self.value

class Device(models.Model):
    qrcode = models.CharField(max_length=200, help_text='二维码')
    code = models.CharField(max_length=50, help_text='编码')
    name = models.CharField(max_length=50, help_text='名称')
    asset_no = models.CharField(max_length=200, null=True, help_text='资产编号')
    specs = models.CharField(max_length=200, null=True, help_text='规格')
    arrival_date = models.DateField(help_text='入厂时间')
    duty_officer = models.CharField(max_length=200, help_text='财产权')
    management_man = models.ForeignKey(Management, models.PROTECT, null=True, help_text='管理单位')
    asset_class = models.ForeignKey(Asset, models.PROTECT, null=True, help_text='资产类别')
    use_status = models.CharField(max_length=200, default='', help_text='设备状态')
    price = models.CharField(max_length=200, null=True, help_text='价格')
    remark = models.CharField(max_length=200, null=True, help_text='备注')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name + ': ' + self.qrcode

USE_STATUS_CHOICES = (
    ('lh', '良好'),
    ('jc', '较差'),
    ('gz', '故障'),
    ('jx', '检修'),
)


# 胶料类型
class JlType(models.Model):
    key = models.CharField(max_length=200, help_text='键名')
    value = models.CharField(max_length=200, help_text='键名')

    def __str__(self):
        return self.key + ': ' + self.value

class Mold(models.Model):
    qrcode = models.CharField(max_length=200, help_text='二维码')
    code = models.CharField(max_length=50, help_text='编码')
    arrival_date = models.DateField(help_text='入厂时间')
    specs = models.CharField(max_length=200, null=True, help_text='规格')
    hole_count = models.CharField(max_length=200, null=True, help_text='穴数')
    duty_officer = models.CharField(max_length=200, help_text='财产权')
    management_man = models.ForeignKey(Management, models.PROTECT, null=True, help_text='管理单位')
    asset_class = models.ForeignKey(Asset, models.PROTECT, null=True, help_text='资产类别')
    jl_type = models.ForeignKey(JlType, models.PROTECT, null=True, help_text='胶料类型')
    jl_dosage = models.CharField(max_length=200, null=True, help_text='胶料用量')
    use_status = models.CharField(max_length=20, choices=USE_STATUS_CHOICES, default='lh', help_text='使用状态')
    location = models.CharField(max_length=200, default='', help_text='位置')
    price = models.CharField(max_length=200, null=True, help_text='价格')
    remark = models.CharField(max_length=200, null=True, help_text='备注')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.code + ': ' + self.qrcode
