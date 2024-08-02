from rest_framework import serializers
from .models import Route, Schedule
from ..buses.models import Bus


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'origin', 'destination', 'distance', 'duration', 'active']


class ScheduleSerializer(serializers.ModelSerializer):
    route = serializers.PrimaryKeyRelatedField(queryset=Route.objects.all())
    bus = serializers.PrimaryKeyRelatedField(queryset=Bus.objects.all())

    class Meta:
        model = Schedule
        fields = ['id', 'route', 'bus', 'departure_time', 'arrival_time', 'price']
