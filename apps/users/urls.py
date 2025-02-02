from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .application.views import ClientViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')

urlpatterns = [
    path('', include(router.urls)),
]
