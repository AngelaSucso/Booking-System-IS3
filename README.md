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
**Pruebas de APIs**
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
    <img src="/Images/postmanPOS.JPG">
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
Casos de Prueba y Resultados:
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


  
## Pruebas de Rendimiento



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

