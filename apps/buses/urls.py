from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BusCompanyViewSet, BusViewSet

router = DefaultRouter()
router.register(r'bus-companies', BusCompanyViewSet)
router.register(r'buses', BusViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
