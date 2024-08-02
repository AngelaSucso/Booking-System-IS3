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

## Objetivo Principal del Proyecto
**Gestión de Reservas y Ventas de Pasajes** 
Desarrollar un sistema que permita a los pasajeros reservar y comprar pasajes.

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

Modelos**
<p align="center">
    <img src="/Images/Models.jpeg">
  </p>

## Pruebas de Software
Pruebas de APIs: Casos de Prueba
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

## Pruebas de Seguridad

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
Cada clase debe tener una única responsabilidad o motivo para cambiar. En otras palabras, una clase debe hacer una cosa y hacerla bien. Esto se puede observar en nuestro proyecto


- O - Open/Closed Principle (OCP):
Las entidades de software deben estar abiertas para su extensión, pero cerradas para su modificación. Esto significa que debes poder añadir nuevas funcionalidades sin cambiar el código existente.  Esto se puede observar en nuestro proyecto


- L - Liskov Substitution Principle (LSP):
Los objetos de una clase derivada deben poder reemplazar a los objetos de la clase base sin alterar el comportamiento del programa. En otras palabras, las subclases deben ser substituibles por sus clases base sin introducir errores. Esto se puede observar en nuestro proyecto



- I - Interface Segregation Principle (ISP):
Los clientes no deben verse obligados a depender de interfaces que no usan. Es mejor tener varias interfaces específicas y pequeñas en lugar de una interfaz grande y general. Esto se puede observar en nuestro proyecto


- D - Dependency Inversion Principle (DIP):
Las dependencias deben ser abstraídas y no depender de implementaciones concretas. Los módulos de alto nivel no deben depender de módulos de bajo nivel, ambos deben depender de abstracciones (interfaces). Esto se puede observar en nuestro proyecto


