from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r'bookings', BookingViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('bookings/create_booking/', BookingViewSet.as_view({'post': 'create_booking'}), name='booking-create-booking'),
    path('payments/create_payment/', PaymentViewSet.as_view({'post': 'create_payment'}), name='payment-create-payment'),
]
