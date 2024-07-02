
from controller.user_controller import UserController
from model.user import User

def main():
    user_controller = UserController()

  
    while True:
        print("\nMenú de Usuario")
        print("1. Crear un nuevo usuario")
        print("2. Eliminar un usuario por ID")
        print("3. Listar todos los usuarios")
        print("4. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            user_id = input("Ingrese el ID del usuario: ")
            name = input("Ingrese el nombre del usuario: ")
            email = input("Ingrese el email del usuario: ")
            new_user = User(user_id, name, email)
            user_controller.save_user(new_user)
            print("Usuario creado exitosamente.")

        elif choice == '2':
            user_id = input("Ingrese el ID del usuario a eliminar: ")
            user_controller.delete_user(user_id)
            print("Usuario eliminado exitosamente.")

        elif choice == '3':
            users = user_controller.get_all_users()
            if users:
                print("Lista de usuarios:")
                for user in users:
                    print(f"ID: {user.get_id()}, Nombre: {user.get_name()}, Email: {user.get_email()}")
            else:
                print("No hay usuarios registrados.")

        elif choice == '4':
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

    
if __name__ == "__main__":
    main()
