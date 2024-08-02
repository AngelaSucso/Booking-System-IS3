from rest_framework import serializers
from apps.users.domain.models.client import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'age']
