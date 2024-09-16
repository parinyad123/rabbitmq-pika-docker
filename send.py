import pika
import ssl

# SSL configuration
# context = ssl.create_default_context(cafile="\certs\ca_certificate.pem")
# context.load_cert_chain(certfile="\certs\client_certificate.pem", keyfile="client_key.pem")
# ssl_options = pika.SSLOptions(context, "localhost")

# ca_file = "C:\Users\parin\programming_projects\rabbitmq\docker_rabbit\certs\ca_certificate.pem"
# client_cert_file = "C:\Users\parin\programming_projects\rabbitmq\docker_rabbit\certs\client_certificate.pem"
# client_key_file = "C:\Users\parin\programming_projects\rabbitmq\docker_rabbit\certs\client_key.pem"

# # SSL configuration
# context = ssl.create_default_context(cafile=ca_file)
# context.verify_mode = ssl.CERT_REQUIRED
# context.load_cert_chain(certfile=client_cert_file, keyfile=client_key_file)
# ssl_options = pika.SSLOptions(context, "localhost")

# Define SSL context
context = ssl.create_default_context(cafile="C:/Users/parin/programming_projects/rabbitmq/docker_rabbit/certs/ca_certificate.pem")
context.verify_mode = ssl.CERT_REQUIRED
context.load_cert_chain(certfile="C:/Users/parin/programming_projects/rabbitmq/docker_rabbit/certs/client_certificate.pem",
                        keyfile="C:/Users/parin/programming_projects/rabbitmq/docker_rabbit/certs/client_key.pem")

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
