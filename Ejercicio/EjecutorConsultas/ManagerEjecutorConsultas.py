from Entidades.DatosConsulta import DatosConsulta
import pika

"""Orquestador de la ejecución de comnsultas por medio del envío de notificaciones a RabbitMQ."""
def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    ObjDocumento = DatosConsulta("123456789", 1, "Colombia")
    Mensaje = ObjDocumento.SerializarAJson()
    for i in range(1, 11):
        channel.queue_declare(queue=f'Fuente No. {i}')
        channel.basic_publish(exchange='',
                              routing_key=f'Fuente No. {i}',
                              body=Mensaje)
        print(f" [x] Se envía consulta a fuente {i} '{Mensaje}'")

    connection.close()

if __name__ == '__main__':
    main()