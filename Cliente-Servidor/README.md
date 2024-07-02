
# Proyecto de Mensajería Cliente-Servidor

Este proyecto es un ejemplo de una aplicación de mensajería basada en la arquitectura cliente-servidor utilizando Python. Permite a múltiples clientes conectarse a un servidor y enviar mensajes que serán retransmitidos a todos los demás clientes conectados.

## Estructura del Proyecto

```plaintext
CLIENTE-SERVIDOR/
── src/
│   ── server/
│   │   ── server.py
│   ── client/
│   │   ── client.py
─── main.py
```

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/tu-usuario/arquitectura-software.git
    cd arquitectura-software
    cd Cliente-servidor
    ```


### Funcionamiento del Servidor

El servidor se ejecutará en un hilo separado y escuchará en el puerto 55555. Aceptará conexiones de clientes y retransmitirá los mensajes recibidos a todos los demás clientes conectados.

### Funcionamiento del Cliente

El cliente se conectará al servidor, permitirá al usuario enviar mensajes y recibirá mensajes retransmitidos por el servidor.

## Ejemplo de Uso

1. Inicia el servidor en una consola:

    ```bash
    python .\src\server\server.py
    ```

1. Inicia los clientes en las consola que desees:

    ```bash
    python .\src\client\client.py
    ```


2. En la consola del cliente, envía y recibe mensajes:

    ```plaintext
    Ingresa tu nombre de usuario: AJCU15
    New message: Hola a todos
    Conectado al servidor  #Indica la conexion al servidor
    Chatbot:Carvjl9se ha unido al chat  #Indica cuando un nuevio cliente se conecta el servidor
    Ingresa tu mensaje: hola como estan? #Se envia el mensaje a todas las persona conectadas
    ```


2. En la consola del servidor,se pueden ver las personas conectadas desde los respectivos puertos:
  ```bash
    Server running on localhost:55555
    AJCU15 est conectado en la direccion ('127.0.0.1', 64262)  
    Carvajl9 est conectado en la direccion ('127.0.0.1', 64272)
    ```