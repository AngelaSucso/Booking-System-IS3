from apps.users.domain.models.client import Client


class ClientRepository:
    @staticmethod
    def get_all():
        return Client.objects.all()

    @staticmethod
    def get_by_id(client_id):
        return Client.objects.get(id=client_id)

    @staticmethod
    def create(client_data):
        return Client.objects.create(**client_data)

    @staticmethod
    def update(client, client_data):
        for key, value in client_data.items():
            setattr(client, key, value)
        client.save()
        return client

    @staticmethod
    def delete(client):
        client.delete()
