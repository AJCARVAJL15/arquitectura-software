
# Proyecto de Mensajería Arquitectura orientada a eventos

Este proyecto en Python demuestra una aplicación simple de mensajería utilizando una arquitectura orientada a eventos. Los usuarios pueden enviar mensajes, los cuales son procesados y registrados utilizando señales de eventos gestionadas por `pydispatch`.

## Características

- **Interacción de Usuario:** Los usuarios (clase `User`) pueden enviar mensajes mediante entrada desde la consola.
- **Procesamiento de Mensajes:** Los mensajes son procesados (clase `MessageProcessor`) convirtiéndolos a mayúsculas.
- **Registro (Logging):** Se registran (clase `Logger`) los mensajes enviados por los usuarios y los mensajes procesados.
- **Cierre del Chat:** Los usuarios pueden cerrar la sesión del chat escribiendo "exit".

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/tu-usuario/arquitectura-software.git
    cd arquitectura-software
    cd Eeventos
    ```
2. Instalar librerias

    - Instala `pydispatch` usando pip:
     ```
     pip install PyDispatcher
     ```

## Ejecutar la Aplicación
   - Ejecuta el script de Python (`main.py`):
     ```
     python main.py
     ```


