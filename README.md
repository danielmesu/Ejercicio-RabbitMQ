# Taller RabbitMQ python
Este repositorio contiene un caso de uso que define una serie de fuentes de información que simulan la ejecución de una consulta. Dicha ejecución se desencadena mediante la recepción de un mensaje de RabbitMQ en colas de mensajes nombradas según la fuente de información, esto con el fin de controlar que consultas se hacen a determinadas fuentes; cada fuente de información escribe a una cola de mensaje transversal un mensaje con el resultado de la consulta en caso de que este sea exitoso. El manager ejecutor de consultas se encarga de orquestar la ejecución de consultas mediante la escritura de mensajes a RabbitMQ en colas de mensajes específicas, en este caso se define un ciclo de 1 a 10 en donde el manager escribe a 10 colas distintas, la responsabilidad de ejecutar las consultas dependerá de las fuentes existentes. Por último, el receptor de resultados se encarga de imprimir los resultados exitosos cada vez que una fuente de información escribe un resultado exitoso a la cola de mensaje transversal. 

Este caso puede ser implementado por un sistema concentrador de datos que depende de la recepción de información de fuentes externas o proveedores de información externos, su arquitectura enfocada a eventos y el uso de adaptadores permite tener múltiples fuentes conectadas al servicio principal sin ser necesarias peticiones HTTP entre microservicios para la ejecución de las consultas. Además de ser un diseño escalable, dado que pueden existir tantos adaptadores como sea necesario sin requerir establecer configuraciones o crear credenciales por cada uno, lo único necesario es establecer el nombre de la cola de menaje que servirá como bus de comunicación entre servicios. 

## Autor
- Daniel Santiago Melo Suárez.

## Ubicación del ejercicio
- Ejercicio/EjecutorConsultas

## Componentes
- **ManagerReceptorResultados.py**
    Responsable de escuchar la cola de mensaje transversal "ResultadoConsultas" y ejecutar la lógica de negocio necesaria con cada resultado exitoso. 
    
- **ManagerEjecutorConsultas.py**
    Responsable de orquestar la ejecución de consultas a las fuentes de información, escribiendo los datos de la consulta a cada cola de mensajes específica según el formato definido por el sistema y el id de las posibles fuentes de información.
    
- **FuenteBase.py**
    Clase abstracta que define las propiedades y métodos que tendrá cualquier fuente de información, incluyendo la construcción de su nombre, la escucha de las notificaciones, la ejecución de consultas y la escritura del resultado a la cola de mensaje transversal "ResultadoConsultas" si el resultado de la consulta fue exitoso.
    
- **FuenteNo1.py / FuenteNo2.py / FuenteNo3.py**
    Fuentes de información existentes y disponibles en el sistema, se comportan como adaptadores para ejecutar consultas con base en la lógica expuesta por los posibles proveedores de información de cada una de ellas.
