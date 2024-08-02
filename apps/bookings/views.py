from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from apps.routes.models import Schedule
from .models import Booking, Payment
from .serializers import BookingSerializer, PaymentSerializer
from apps.users.domain.models.client import Client


# Create your views here.
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    @action(detail=False, methods=['post'])
    def create_booking(self, request):
        # user = request.user
        client_id = request.data.get('client_id')
        schedule_id = request.data.get('schedule_id')
        seat_number = request.data.get('seat_number')

        if not schedule_id or not seat_number:
            return Response({"error": "schedule_id and seat_number are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return Response({"error": "Invalid client_id"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            schedule = Schedule.objects.get(id=schedule_id)
        except Schedule.DoesNotExist:
            return Response({"error": "Invalid schedule_id"}, status=status.HTTP_404_NOT_FOUND)

        booking = Booking.objects.create(
            client=client,
            schedule=schedule,
            seat_number=seat_number,
            status='pending'
        )
        return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    @action(detail=False, methods=['post'])
    def create_payment(self, request):
        booking_id = request.data.get('booking_id')
        amount = request.data.get('amount')
        payment_method = request.data.get('payment_method')
        transaction_id = request.data.get('transaction_id')

        if not booking_id or not amount or not payment_method or not transaction_id:
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            booking = Booking.objects.get(id=booking_id)
        except Booking.DoesNotExist:
            return Response({"error": "Invalid booking_id"}, status=status.HTTP_404_NOT_FOUND)

        payment = Payment.objects.create(
            booking=booking,
            amount=amount,
            payment_method=payment_method,
            payment_status='completed',
            transaction_id=transaction_id
        )

        booking.status = 'confirmed'
        booking.save()

        return Response(PaymentSerializer(payment).data, status=status.HTTP_201_CREATED)
