# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Device, Asset, Management, JlType, Mold

# Register your models here.
admin.site.register(Device)
admin.site.register(Asset)
admin.site.register(Management)
admin.site.register(JlType)
admin.site.register(Mold)
