from rest_framework import viewsets
from .models import Bus, BusCompany
from .serializers import BusSerializer, BusCompanySerializer


# Create your views here.
class BusCompanyViewSet(viewsets.ModelViewSet):
    queryset = BusCompany.objects.all()
    serializer_class = BusCompanySerializer


class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
