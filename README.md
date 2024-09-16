# RabbitMQ SSL Project

This project demonstrates how to set up RabbitMQ with SSL using Docker and connect to it via Python scripts (`send.py` and `receive.py`).

## Setup Instructions

### 1. Generate SSL Certificates

Generate the necessary certificates using the following commands:

```bash
# Generate CA certificate
openssl req -new -x509 -days 3650 -keyout certs/ca_key.pem -out certs/ca_certificate.pem -nodes -subj "/C=TH/ST=Bangkok/L=Bangkok/O=TRUS/OU=POC/CN=MyRabbitMQCA"

# Generate server certificate
openssl genrsa -out certs/server_key.pem 2048
openssl req -new -key certs/server_key.pem -out certs/server_csr.pem -subj "/C=TH/ST=Bangkok/L=Bangkok/O=TRUS/OU=POC/CN=localhost"
openssl x509 -req -in certs/server_csr.pem -CA certs/ca_certificate.pem -CAkey certs/ca_key.pem -CAcreateserial -out certs/server_certificate.pem -days 3650

# Generate client certificate
openssl genrsa -out certs/client_key.pem 2048
openssl req -new -key certs/client_key.pem -out certs/client_csr.pem -subj "/C=TH/ST=Bangkok/L=Bangkok/O=TRUS/OU=POC/CN=client"
openssl x509 -req -in certs/client_csr.pem -CA certs/ca_certificate.pem -CAkey certs/ca_key.pem -CAcreateserial -out certs/client_certificate.pem -days 3650
```
