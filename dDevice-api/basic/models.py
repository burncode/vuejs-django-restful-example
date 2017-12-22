from django.db import models

# 供应商
class Supplier(models.Model):
    code = models.CharField(max_length=50, help_text='编码')
    name = models.CharField(max_length=50, help_text='名称')
    phone = models.CharField(max_length=50, null=True, help_text='电话')
    address = models.CharField(max_length=200, null=True, help_text='地址')
    remark = models.CharField(max_length=200, null=True, help_text='描述')

    def __str__(self):
        return self.code + ': ' + self.name

# 工厂管理
class Organization(models.Model):
    code = models.CharField(max_length=50, help_text='编码')
    name = models.CharField(max_length=50, help_text='名称')
    manager = models.CharField(max_length=50, null=True, help_text='负责人')
    phone = models.CharField(max_length=50, null=True, help_text='电话')
    address = models.CharField(max_length=200, null=True, help_text='地址')
    remark = models.CharField(max_length=200, null=True, help_text='描述')

    def __str__(self):
        return self.code + ': ' + self.name
