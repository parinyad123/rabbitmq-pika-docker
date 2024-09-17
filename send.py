import pika
import ssl

# SSL configuration
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

# Connect to RabbitMQ and send a message
with pika.BlockingConnection(connection_params) as connection:
    channel = connection.channel()
    channel.queue_declare(queue='test_queue')
    channel.basic_publish(exchange='', routing_key='test_queue', body='Hello, RabbitMQ with SSL!')
    print("Message sent!")
