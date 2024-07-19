# Servicios SOA con Flask

Este proyecto implementa un sistema simple de servicios SOA utilizando Flask. Incluye dos servicios principales: un servicio de usuario y un servicio de autenticación.

## Requisitos

- Python 3.11.9
- Flask



## Ejecución de los Servicios

1. Ejecuta el servicio de usuario:
    ```bash
    python user_service.py
    ```


2. Ejecuta el servicio de autenticación:
    ```bash
    python auth_service.py
    ```

## Uso de `curl` para Probar los Servicios

### Crear un Usuario


curl -X POST http://localhost:5000/create_user -H "Content-Type: application/json" -d '{"id": "1", "name": "John Doe"}'
### obtener un Usuario

curl http://localhost:5000/get_user/1

### autenticar un un Usuario
curl http://localhost:5000/get_user/1




