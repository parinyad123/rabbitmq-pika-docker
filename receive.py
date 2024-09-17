import pika
import ssl

# # SSL configuration
context = ssl.create_default_context(cafile="./certs/ca_certificate.pem")
context.verify_mode = ssl.CERT_REQUIRED
context.load_cert_chain(certfile="./certs/client_certificate.pem",
                        keyfile="./certs/client_key.pem")

ssl_options = pika.SSLOptions(context, "localhost")

# Connection parameters
connection_params = pika.ConnectionParameters(
    port=5671,  # SSL port
    ssl_options=ssl_options
)

# Connect to RabbitMQ and receive messages
with pika.BlockingConnection(connection_params) as connection:
    channel = connection.channel()
    channel.queue_declare(queue='test_queue')

    def callback(ch, method, properties, body):
        print(f"Received: {body.decode()}")

    channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=True)
    print('Waiting for messages...')
    channel.start_consuming()
