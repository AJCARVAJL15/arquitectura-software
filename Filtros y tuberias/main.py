from src.tuberias import Tuberia
from src.filtros import *



tuberia=Tuberia()

tuberia.agregar_filtro(filtro_sumar,5)
tuberia.agregar_filtro(filtro_multiplicar,4)
tuberia.agregar_filtro(filtro_dividir,5)


dato_inicial=5
dato_final=tuberia.procesar(dato_inicial)

print(f"Dato inicial: {dato_inicial}")
print(f"Dato final: {dato_final}")