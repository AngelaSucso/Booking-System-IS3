from apps.users.infrastructure.repositories.client_repository import ClientRepository


class ClientService:
    def __init__(self):
        self.client_repository = ClientRepository()

    def get_all_clients(self):
        return self.client_repository.get_all()

    def get_client_by_id(self, client_id):
        return self.client_repository.get_by_id(client_id)

    def create_client(self, client_data):
        return self.client_repository.create(client_data)

    def update_client(self, client_id, client_data):
        client = self.client_repository.get_by_id(client_id)
        return self.client_repository.update(client, client_data)

    def delete_client(self, client_id):
        client = self.client_repository.get_by_id(client_id)
        self.client_repository.delete(client)
