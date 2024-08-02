from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from apps.users.domain.services.client_service import ClientService
from apps.users.infrastructure.serializers import ClientSerializer


class ClientViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client_service = ClientService()

    def list(self, request):
        clients = self.client_service.get_all_clients()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        client = self.client_service.get_client_by_id(pk)
        if client is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def create(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            client = self.client_service.create_client(serializer.validated_data)
            return Response(ClientSerializer(client).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            client = self.client_service.update_client(pk, serializer.validated_data)
            return Response(ClientSerializer(client).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        self.client_service.delete_client(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
