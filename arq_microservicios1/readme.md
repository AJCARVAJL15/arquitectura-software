# Ejemplo de Arquitectura de Microservicios en Python

Este proyecto demuestra una arquitectura usando Flask. Consta de dos microservicios: uno para manejar mensajes (Servicio de Mensajes) y otro para manejar saludos (Servicio de Saludos). También hay un script cliente que interactúa con ambos microservicios.

## Estructura del Proyecto

- `mensaje.py`: Maneja los mensajes.
- `saludos.py`: Maneja los saludos.
- `cliente.py`: Script cliente para interactuar con los microservicios.

## Requisitos

- Python 3.11.9
- Flask
- requests



## Ejecutando los Microservicios

1. **Abre el primer terminal y ejecuta el Servicio de Mensajes:**

    python mensaje.py

    salida  que el servicio se está ejecutando en `http://127.0.0.1:5001`.

2. **Abre el segundo terminal y ejecuta el Servicio de Saludos:**

    python saludos.py

    salida  que el servicio se está ejecutando en `http://127.0.0.1:5002`.

## Ejecutando el Cliente

Abre un tercer terminal y ejecuta el script del cliente:

python cliente.py

## Salida esperada
Messages: 200, [{'id': 1, 'text': 'Holaa'}, {'id': 2, 'text': 'buenos dias'}]
Greetings: 200, [{'id': 1, 'text': 'Hola estoy aqui'}, {'id': 2, 'text': 'saludos!'}]
