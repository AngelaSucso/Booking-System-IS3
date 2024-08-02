from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.urls import reverse
from .models import Booking, Payment
from apps.users.domain.models.client import Client

from apps.routes.models import Schedule, Route
from apps.buses.models import Bus, BusCompany


# Create your tests here.


class BookingTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        self.client_user = Client.objects.create(first_name='testname', last_name='testlastname', age='18')
        self.bus_company = BusCompany.objects.create(name="Test Company", address="Test Address",
                                                     phone_number="123456789", email="test@test.com")
        self.bus = Bus.objects.create(license_plate="123ABC", bus_model="Model X", capacity=50,
                                      company=self.bus_company)
        self.route = Route.objects.create(origin="City A", destination="City B", distance=100, duration=120,
                                          active=True)
        self.schedule = Schedule.objects.create(route=self.route, bus=self.bus, departure_time="2024-12-01T10:00:00Z",
                                                arrival_time="2024-12-01T12:00:00Z", price=100.00)

    def test_create_booking(self):
        url = reverse('booking-create-booking')
        data = {'client_id': self.client_user.id, 'schedule_id': self.schedule.id, 'seat_number': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(Booking.objects.get().seat_number, 1)

    def test_create_payment(self):
        booking = Booking.objects.create(client=self.client_user, schedule=self.schedule, seat_number=1,
                                         status='pending')
        url = reverse('payment-create-payment')
        data = {'booking_id': booking.id, 'amount': 100.00, 'payment_method': 'credit_card',
                'transaction_id': 'txn_12345'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Payment.objects.count(), 1)
        self.assertEqual(Payment.objects.get().payment_method, 'credit_card')
