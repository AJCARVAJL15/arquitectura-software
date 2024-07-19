# Ejemplo de Blockchain en Python

Este proyecto demuestra una implementación simple de una blockchain y una red básica de peer-to-peer (P2P) usando Python y Flask.

## Archivos

- `blockchain.py`: Contiene la clase `Blockchain`, que gestiona la blockchain y sus transacciones.
- `node.py`: Contiene la aplicación Flask que proporciona una API para interactuar con la blockchain y gestionar nodos en la red P2P.


## Endpoints de la API

1. Minar un Nuevo Bloque


    Endpoint: /mine
    Método: GET

    Este endpoint mina un nuevo bloque y lo agrega a la blockchain.

    Respuesta:
    ```bash
        {
        "message": "Nuevo Bloque Forjado",
        "index": 2,
        "transactions": [],
        "proof": 35293,
        "previous_hash": "1d1d03c4f26d8b30dd407e80d9d45e56d31b7d9c33cb1e1678b5d872df8b86c0"
    }
        ```

2. Crear una Nueva Transacción
    Endpoint: /transactions/new
    Método: POST

    Este endpoint crea una nueva transacción para ser añadida al próximo bloque minado.

     Cuerpo de la solicitud:
    ```bash
        {
        "sender": "direccion_del_remitente",
        "recipient": "direccion_del_destinatario",
        "amount": 10
        }
    ```

    Respuesta:
    ```bash
        {
        "message": "La transacción será añadida al Bloque 2"
        }
        ```

3. Obtener la Blockchain Completa
    Endpoint: /chain
    Método: GET

    Este endpoint devuelve toda la blockchain.

    Respuesta:
    ```bash 
        {
        "chain": [...],
        "length": 2
        }
    ```

4. Registrar Nuevos Nodos
    Endpoint: /nodes/register
    Método: POST

    Este endpoint registra nuevos nodos en la red.

    Cuerpo de la Solicitud:
     ```bash 
        {
        "nodes": ["http://127.0.0.1:5001"]
        }
    ```

    Respuesta 
     ```bash 
        {
        "message": "Nuevos nodos han sido añadidos",
        "total_nodes": ["http://127.0.0.1:5001"]
        }
    ```

5. Algoritmo de Consenso
    Endpoint: /nodes/resolve
    Método: GET

    Este endpoint ejecuta el algoritmo de consenso, resolviendo conflictos y asegurando que todos los nodos tengan la cadena correcta.

    Respuesta:
    ```bash 
     {
    "message": "Nuestra cadena es autoritativa",
    "chain": [...]
    }
    ```

## Simular red P2P

1. Iniciar Múltiples Nodos:
    Ejecuta múltiples instancias de node.py en diferentes puertos.

    ```bash 
        python node.py # Puerto por defecto 5000
        python node.py -p 5001 # Puerto personalizado 5001
     ```

2. Registrar Nodos:
    Registra nodos entre sí para establecer la red.

    ```bash 
     curl -X POST -H "Content-Type: application/json" -d '{"nodes":["http://127.0.0.1:5001"]}' "http://127.0.0.1:5000/nodes/register"
    ```

3. Minar y Añadir Transacciones:

    Usa los endpoints /mine y /transactions/new para añadir transacciones y minar nuevos bloques. Cada nodo verificará independientemente y añadirá bloques a su cadena.

    Resolver Conflictos:
    Usa el endpoint /nodes/resolve para asegurar que todos los nodos tengan la cadena correcta y más actualizada.

    ```bash 
        curl -X GET "http://127.0.0.1:5000/nodes/resolve"
    ```
