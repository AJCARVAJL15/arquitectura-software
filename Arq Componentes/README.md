# Gym Manager

Este es un ejemplo de un sistema de gestión de ingreso de personas a un gimnasio utilizando una arquitectura de componentes en Python.



## Descripción de Componentes

### models/member.py

Define la clase `Member` que representa un miembro del gimnasio.

### services/member_service.py

Maneja las operaciones relacionadas con los miembros, como obtener la lista de miembros, obtener detalles de un miembro específico y registrar la entrada de un miembro.

### components/check_in.py

Se encarga de registrar la entrada de un miembro y emite una señal cuando un miembro se registra con éxito.

### components/member_detail.py

Escucha la señal de registro de entrada y muestra los detalles del miembro registrado.

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu_usuario/arquitectura-software.git
    cd arquitectura-software
    cd Arq Componentes
    ```

2. Crea un entorno virtual:

    ```bash
    python -m venv env
    source env/bin/activate 
    ```

3. Instala las dependencias:

    ```bash
    pip install pydispatch
    ```

## Ejecución

Ejecuta el archivo `main.py` para iniciar el sistema de gestión de ingreso:

```bash
python main.py
```

