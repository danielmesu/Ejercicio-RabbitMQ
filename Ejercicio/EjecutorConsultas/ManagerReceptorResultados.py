from Entidades.DatosConsulta import DatosConsulta
import pika

"""Receptor de resultados exitosos de las consultas a las fuentes de información por medio de notificaciones de RabbitMQ."""
def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='ResultadoConsultas')

    def callback(ch, method, properties, body):
        print(f'Se ha recibido una consulta exitosa: {body}')

    channel.basic_consume(queue='ResultadoConsultas', on_message_callback=callback, auto_ack=True)

    print(F' [*] Receptor de resultados activado.')
    channel.start_consuming()

if __name__ == '__main__':
    main()