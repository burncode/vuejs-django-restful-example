from django.conf.urls import url, include
from rest_framework import routers
from .views import SupplierViewSet, OrganizationViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'^suppliers', SupplierViewSet, base_name='supplier')
router.register(r'^organizations', OrganizationViewSet, base_name='organization')

urlpatterns = [
    url(r'', include(router.urls))
]
