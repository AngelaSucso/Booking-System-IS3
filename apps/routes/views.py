from rest_framework import viewsets
from .models import Route, Schedule
from .serializers import RouteSerializer, ScheduleSerializer


# Create your views here.
class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
