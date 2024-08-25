import pika 
import random
from abc import ABC, abstractmethod
from Entidades.DatosConsulta import DatosConsulta

"""Clase abstracta que define los métodos compartidos que tendrá cualquier clase que se comporte como fuente de información."""
class FuenteBase(ABC):

    """Propiedad que define el número de la fuente."""
    @property
    @abstractmethod
    def NumeroFuente(self):
        pass

    """Obtiene el nombre de la fuente para establecer el nombre de la cola de mensaje."""
    def ObtenerNombreFuente(self):
        return f"Fuente No. {self.NumeroFuente}"
    

    """Método que escucha las notificaciones de RabbigMQ."""
    def EscucharNotificación(self):
          StrNombreCola = self.ObtenerNombreFuente()
          connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
          channel = connection.channel()

          channel.queue_declare(queue=StrNombreCola)

          def callback(ch, method, properties, body):
            self.EjecutarConsulta(body)

          channel.basic_consume(queue=StrNombreCola, on_message_callback=callback, auto_ack=True)

          channel.start_consuming()

    
    """Método que simula la ejcución de una consulta y establece un valor booleano al resultado de la misma."""
    def EjecutarConsulta(self, PrmStrBody):
         try:
            ObjDatosConsulta = DatosConsulta.ConvertirDesdeJson(PrmStrBody)
            BlnResultado = random.choice([True, False])
            print(f" [x] Se ha consultado a {self.ObtenerNombreFuente()}, el número consultado es {ObjDatosConsulta.NumeroDocumento} y el resultado fue {BlnResultado}")
            if BlnResultado:
                self.EscribirResultado(ObjDatosConsulta, self.NumeroFuente)
         except Exception as e:
            print(f"Error al procesar la consulta: {e}")


    """Método que envía una notificación a RabbitMQ con el resulado de una consulta exitosa."""
    def EscribirResultado(self, PrmObjDatosConsultados: DatosConsulta, PrmIntIdFuente: int):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='ResultadoConsultas')
        Mensaje = f"Consulta documento {PrmObjDatosConsultados.NumeroDocumento}, resultado exitoso, Id de fuente que responde {PrmIntIdFuente}"
        channel.basic_publish(exchange='',
                              routing_key='ResultadoConsultas',
                              body=Mensaje)
        connection.close()