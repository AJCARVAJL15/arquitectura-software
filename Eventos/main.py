from pydispatch import dispatcher

EVENTO_ENVIAR_MENSAJE = 'evento_enviar_mensaje'
EVENTO_PROCESAR_MENSAJE = 'evento_procesar_mensaje'
EVENTO_CERRAR_CHAT = 'evento_cerrar_chat'

class User:
    def __init__(self, nombre):
        self.nombre = nombre

    def enviar_mensaje(self):
        mensaje = input(f"{self.nombre}, escribe tu mensaje ('exit' para salir): ")
        if mensaje.lower() == 'exit':
            dispatcher.send(signal=EVENTO_CERRAR_CHAT, sender=self)

            return False
        print(f"{self.nombre} está enviando un mensaje: {mensaje}")
        dispatcher.send(signal=EVENTO_ENVIAR_MENSAJE, sender=self, mensaje=mensaje)
        return True



class MessageProcessor:
    def __init__(self):
        dispatcher.connect(self.procesar_mensaje, signal=EVENTO_ENVIAR_MENSAJE)

    def procesar_mensaje(self, sender, mensaje):
        print(f"Procesando mensaje: {mensaje}")
        mensaje_procesado = mensaje.upper()
        dispatcher.send(signal=EVENTO_PROCESAR_MENSAJE, sender=self, mensaje_procesado=mensaje_procesado)


class Logger:
    def __init__(self):
        dispatcher.connect(self.registrar_log, signal=EVENTO_ENVIAR_MENSAJE)
        dispatcher.connect(self.registrar_log, signal=EVENTO_PROCESAR_MENSAJE)
        dispatcher.connect(self.cerrar_chat, signal=EVENTO_CERRAR_CHAT)
    def registrar_log(self, sender, **kwargs):
        if 'mensaje' in kwargs:
            print(f"LOG: {sender.nombre} envió el mensaje: {kwargs['mensaje']}")
        if 'mensaje_procesado' in kwargs:
            print(f"LOG: Mensaje procesado: {kwargs['mensaje_procesado']}")

    def cerrar_chat(self, sender):
         print(f"CHAT CERRADO por {sender.nombre}")


user1 = User('User1')
user2 = User('User2')
processor = MessageProcessor()
logger = Logger()

while True:
    if not user1.enviar_mensaje():
        break
    if not user2.enviar_mensaje():
        break


dispatcher.disconnect(processor.procesar_mensaje, signal=EVENTO_ENVIAR_MENSAJE)
dispatcher.disconnect(logger.registrar_log, signal=EVENTO_ENVIAR_MENSAJE)
dispatcher.disconnect(logger.registrar_log, signal=EVENTO_PROCESAR_MENSAJE)
