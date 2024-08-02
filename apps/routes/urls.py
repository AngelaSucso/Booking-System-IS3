from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RouteViewSet, ScheduleViewSet

router = DefaultRouter()
router.register(r'routes', RouteViewSet)
router.register(r'schedules', ScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
