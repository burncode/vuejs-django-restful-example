from django.conf.urls import url, include
from rest_framework import routers
from .views import AssetViewSet, ManagementViewSet, DeviceViewSet, MoldViewSet, JlTypeViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'^assets', AssetViewSet, base_name='asset')
router.register(r'^managements', ManagementViewSet, base_name='management')
router.register(r'^devices', DeviceViewSet, base_name='device')
router.register(r'^molds', MoldViewSet, base_name='mold')
router.register(r'^jl-types', JlTypeViewSet, base_name='jl-type')

urlpatterns = [
    url(r'', include(router.urls))
]
