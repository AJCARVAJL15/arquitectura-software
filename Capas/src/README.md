# Proyecto de Gestión de Usuarios en Python

Este proyecto es una implementación básica de un sistema de gestión de usuarios utilizando una arquitectura de capas en Python.

## Estructura del Proyecto

La estructura del proyecto sigue una arquitectura de capas, separando las responsabilidades en diferentes módulos:


```plaintext
Capas/
└── src/
├── controller/
│ └── user_controller.py
├── service/
│ └── user_service.py
├── repository/
│ └── user_repository.py
├── model/
│ └── user.py
└── main.py
```

### Capas del Proyecto

1. **Modelo (`model`):**
    - `user.py`: Define la clase `User` con sus atributos y métodos.

2. **Repositorio (`repository`):**
    - `user_repository.py`: Gestiona el almacenamiento y recuperación de datos de los usuarios.

3. **Servicio (`service`):**
    - `user_service.py`: Contiene la lógica para gestionar usuarios, utilizando el repositorio.

4. **Controlador (`controller`):**
    - `user_controller.py`: Maneja las interacciones con el usuario y llama a los servicios apropiados.

5. **Main (`main`):**
    - `main.py`: Punto de entrada del programa que presenta un menú para gestionar usuarios.



## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu_usuario/arquitectura-software.git
    cd arquitectura-software
    cd Capas
    ```



## Ejecución del Proyecto


1. Ejecuta el script principal:

    ```bash
    python src/main.py
    ```

2. Interactúa con el menú presentado para gestionar los usuarios:

    ```bash
    Menu de opciones:
    1. Crear usuario
    2. Eliminar usuario
    3. Ver usuario
    4. Salir
    Seleccione una opción: 
    ```

## Uso del Menú

### Crear Usuario

1. Selecciona la opción `1` en el menú.
2. Ingresa el ID, nombre y email del usuario cuando se te solicite.
3. Verás un mensaje confirmando la creación del usuario.

### Eliminar Usuario

1. Selecciona la opción `2` en el menú.
2. Ingresa el ID del usuario que deseas eliminar.
3. Verás un mensaje confirmando la eliminación del usuario.

### Ver Usuarios

1. Selecciona la opción `3` en el menú.
2. Se observan todos los usaurios registrados.

### Ver Usuarios

1. Selecciona la opción `4` para salir del programa.

