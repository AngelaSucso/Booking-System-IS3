from rest_framework import serializers
from .models import Bus, BusCompany


class BusCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusCompany
        fields = ['id', 'name', 'address', 'phone_number', 'email']


class BusSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=BusCompany.objects.all())

    class Meta:
        model = Bus
        fields = ['id', 'license_plate', 'bus_model', 'capacity', 'company', 'active']
