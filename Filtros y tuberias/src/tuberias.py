class Tuberia:
    def __init__(self):
        self.filtros = []
    
    def agregar_filtro(self, filtro, *args):
        self.filtros.append((filtro, args))
    
    def procesar(self, dato_inicial):
        dato = dato_inicial
        for filtro, args in self.filtros:
            dato = filtro(dato, *args)
        return dato
