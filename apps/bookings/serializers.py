from rest_framework import serializers
from .models import Booking, Payment
from apps.users.domain.models.client import Client


class BookingSerializer(serializers.ModelSerializer):
    schedule = serializers.StringRelatedField()
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())

    class Meta:
        model = Booking
        fields = ['id', 'client', 'schedule', 'seat_number', 'booking_time', 'status']


class PaymentSerializer(serializers.ModelSerializer):
    booking = serializers.StringRelatedField()

    class Meta:
        model = Payment
        fields = ['id', 'booking', 'amount', 'payment_method', 'payment_status', 'transaction_id']
