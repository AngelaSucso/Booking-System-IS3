#  Sistema Gestión de Pasajes (SGP)

## Integrantes:
- Evelyn Lizbeth, Cusi Hancco
- Angela Solange, Sucso Choque

## Cliente
- Nombre Empresa: Cruz Del Sur
- Dirección Legal: Av. Francisco Bolognesi Nro. 495 Zona Industrial (Espalda Centro Bancario Sta. Anita)
- Razón Social: TRANSPORTES CRUZ DEL SUR S.A.C.
- Tipo Empresa: Sociedad Anonima
- RUC: 20100227461
- Página Web: http://www.cruzdelsur.com.pe

## Propósito del proyecto
Se tiene como propósito definir las especificaciones (requisitos) funcionales y no funcionales para el desarrollo de un sistema de reservas y gestión de pasajeros que permitirá gestionar distintos procesos relacionados con la reserva, venta y seguimiento de pasajes de transporte en la empresa Cruz del Sur S.A.C. Este sistema será utilizado por los pasajeros que deseen reservar y comprar pasajes para viajar en los servicios ofrecidos por la empresa.

**Objetivo Principal del Proyecto**
- Gestión de Reservas y Ventas de Pasajes: Desarrollar un sistema que permita a los pasajeros reservar y comprar pasajes.

# Domain-Driven Design (DDD) Explanation

## Domain Layer (Capa de Dominio)

### Responsabilidad
La capa de dominio define los conceptos y reglas del negocio. Esta capa no debe depender de las capas de infraestructura o aplicación.

### Componentes

- **Models**: Representan los objetos de negocio y sus relaciones. En nuestro proyecto, `Client` es un modelo de dominio.
- **Services**: Contienen la lógica de negocio que no encaja naturalmente dentro de los modelos. Por ejemplo, `client_service.py` contiene lógica para crear, actualizar o validar clientes.

## Application Layer (Capa de Aplicación)

### Responsabilidad
La capa de aplicación define cómo se utiliza el dominio. Orquesta las tareas y maneja los casos de uso del sistema. Interactúa con la capa de infraestructura para obtener datos necesarios.

### Componentes

- **Views**: Manejan las solicitudes HTTP y llaman a los servicios de aplicación o de dominio para realizar operaciones. En nuestra estructura, `views.py` contiene las vistas relacionadas con los clientes.

## Infrastructure Layer (Capa de Infraestructura)

### Responsabilidad
La capa de infraestructura proporciona implementaciones técnicas para interactuar con sistemas externos. Implementa repositorios, serializers y otros adaptadores.

### Componentes

- **Repositories**: Implementan la persistencia de los modelos de dominio. `client_repository.py` maneja las operaciones CRUD para el modelo `Client`.
- **Serializers**: Transforman los modelos de dominio en formatos compatibles con JSON y viceversa. `serializers.py` contiene los serializers para los modelos de dominio.


## Estructura de Carpetas

<p align="center">
    <img src="/Images/Estructura.jpeg">
  </p>


# Patrones de Arquitectura


El proyecto sigue el patrón **MVC (Model-View-Controller)**, que es típico en aplicaciones Django. Sin embargo, la aplicación `users` está estructurada siguiendo los principios de **arquitectura por capas (Presentación, Aplicación, Dominio, Repositorio)** de DDD.

### Capas de la Arquitectura

1. **Presentación**:
   - Responsable de manejar las interacciones con el usuario.
   - En nuestro caso, esto está implementado en `views.py` de la aplicación `users`.

2. **Aplicación**:
   - Contiene la lógica de negocio y las reglas de la aplicación.
   - En nuestro proyecto, esta lógica está implementada en `client_service.py` dentro de `domain/services/`.

3. **Dominio**:
   - Representa los conceptos centrales y las reglas de negocio del dominio.
   - En este proyecto, los modelos de datos y la lógica de negocio asociada están en `models/client.py`.

4. **Repositorio**:
   - Maneja el acceso a la base de datos.
   - En este proyecto, los repositorios están implementados en `repositories/client_repository.py`.


### Explicación de Cada Parte en DDD


`users/application/views.py`:

```python
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
```

`users/domain/services/client_service.py`:

```python
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
```

`users/domain/models/client.py`:
```python
from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

```


`users/domain/models/client.py`:
```python
from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
```
La capa de dominio contiene los modelos de datos y la lógica de negocio central. El modelo `Client` representa un cliente en el sistema.

`users/infrastructure/repositories/client_repository.py`:
```python
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
```

La capa de repositorio maneja el acceso a la base de datos. `ClientRepository` contiene métodos para recuperar datos de los clientes.


## Principios SOLID
- S - Single Responsibility Principle (SRP):
Cada clase debe tener una única responsabilidad o motivo para cambiar. Esto se puede observar en nuestro proyecto:
<p align="center">
    <img src="/Images/SS2.jpeg">
  </p>

- O - Open/Closed Principle (OCP):
Las entidades de software deben estar abiertas para su extensión, pero cerradas para su modificación. Esto se puede observar en nuestro proyecto:
<p align="center">
    <img src="/Images/S3.jpeg">
  </p>

- L - Liskov Substitution Principle (LSP):
Los objetos de una clase derivada deben poder reemplazar a los objetos de la clase base sin alterar el comportamiento del programa. Esto se puede observar en nuestro proyecto:
<p align="center">
    <img src="/Images/S4.jpeg">
  </p>

- I - Interface Segregation Principle (ISP):
Los clientes no deben verse obligados a depender de interfaces que no usan. Esto se puede observar en nuestro proyecto:
<p align="center">
    <img src="/Images/S5.jpeg">
  </p>

- D - Dependency Inversion Principle (DIP):
Las dependencias deben ser abstraídas y no depender de implementaciones concretas. Esto se puede observar en nuestro proyecto:
<p align="center">
    <img src="/Images/SS1.jpeg">
  </p>




## Servicios de Soporte a Tareas Automáticas en Procesos de Negocio
Esta sección detalla cómo se proporcionan servicios de soporte para tareas automatizadas en los procesos de negocio utilizando OpenAPI y la herramienta Swagger.

**Operaciones Disponibles**

| Métodos     |      URL      |                    Parámetros                   |
|-------------|---------------|-------------------------------------------------|
| GET         | api/bookings  | id, client, schedule, seat_number, booking_time |
| POST        | api/bookings  | client, seat_number                             |
| GET         | api/buses     | id, bus_model, capacity, company, activate      |
| POST        | api/buses     | bus_model, capacity, company                    |
| GET         | api/client    | id, origin, destination, distance, duration     |
| POST        | api/client    | origin, destination, distance, duration         |

**Modelos Vista Swagger**
<p align="center">
    <img src="/Images/Models.jpeg">
  </p>

- Booking
<p align="center">
    <img src="/Images/modeloBooking.png">
  </p>

- BusCompany
<p align="center">
    <img src="/Images/modeloBusCompany.png">
  </p>

- Bus
<p align="center">
    <img src="/Images/modeloBus.png">
  </p>

- Payment
<p align="center">
    <img src="/Images/modeloPayment.png">
  </p>

- Route
<p align="center">
    <img src="/Images/modeloRoute.png">
  </p>

- Schedule
<p align="center">
    <img src="/Images/modeloSchedule.png">
  </p>

- TokkenObtainPair
<p align="center">
    <img src="/Images/modeloToken.png">
  </p>

- TokkenRefresh
<p align="center">
    <img src="/Images/modeloTokenRefresh.png">
  </p>

## Pruebas de Software
**Pruebas de APIs**: 
Casos de Prueba y Resultados
- Documentación de Swagger:
<p align="center">
    <img src="/Images/BookingsSwagger.jpeg">
  </p>
<p align="center">
    <img src="/Images/BusesSwagger.jpeg">
  </p>
<p align="center">
    <img src="/Images/RoutesSwagger.jpeg">
  </p>


- Documentación de Postman:
<p align="center">
    <img src="/Images/postman.PNG">
  </p>

<p align="center">
    <img src="/Images/POSpostman.JPG">
  </p>

Test de Api:

```
class BookingTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        self.client_user = Client.objects.create(first_name='testname', 
                                                last_name='testlastname', 
                                                age='18')
        self.bus_company = BusCompany.objects.create(name="Test Company", 
                                                    address="Test Address",
                                                    phone_number="123456789", 
                                                    email="test@test.com")
        self.bus = Bus.objects.create(license_plate="123ABC",
                                      bus_model="Model X",
                                      capacity=50,
                                      company=self.bus_company)                    
        self.route = Route.objects.create(origin="City A",
                                          destination="City B",
                                          distance=100,
                                          duration=120,
                                          active=True)
        self.schedule = Schedule.objects.create(route=self.route,
                                                bus=self.bus,
                                                departure_time="2024-12-01T10:00:00Z",
                                                arrival_time="2024-12-01T12:00:00Z",
                                                price=100.00)
    def test_create_booking(self):
        url = reverse('booking-create-booking')
        data = {'client_id': self.client_user.id, 'schedule_id': self.schedule.id, 'seat_number': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(Booking.objects.get().seat_number, 1)
    def test_create_payment(self):
        booking = Booking.objects.create(client=self.client_user,
                                         schedule=self.schedule,
                                         seat_number=1,
                                         status='pending')
        url = reverse('payment-create-payment')
        data = {'booking_id': booking.id, 'amount': 100.00, 'payment_method': 'credit_card',
                'transaction_id': 'txn_12345'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Payment.objects.count(), 1)
        self.assertEqual(Payment.objects.get().payment_method, 'credit_card')
```     
        
## Pruebas de Seguridad
**Casos de Prueba y Resultados:**
   <p align="center">
    <img src="/Images/E1.jpg">
  </p>

   <p align="center">
    <img src="/Images/E2.jpeg">
  </p>



   <p align="center">
    <img src="/Images/E3.jpeg">
  </p>


   <p align="center">
    <img src="/Images/E4.jpeg">
  </p>


  


