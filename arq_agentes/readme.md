# Proyecto de Arquitectura Basada en Agentes

Este proyecto simula la inteaccion entre dos tipos de agentes, el vendedor y el comprador

## Descripción

En esta simulación, un agente comprador (`BuyerAgent`) intenta comprar un artículo de un agente vendedor (`SellerAgent`). El vendedor ofrece un precio aleatorio para el artículo y el comprador decide si puede comprarlo

## Estructura del Código

- `Agent`: Clase base para todos los agentes.
- `BuyerAgent`: Clase que representa a un agente comprador.
- `SellerAgent`: Clase que representa a un agente vendedor.
- `Simulación`: Instancias de los agentes interactúan en un bucle para realizar múltiples intentos de compra.

## Requisitos

- Python 3.11.9

## Uso

Ejecuta el script principal para iniciar la simulación

## Ejemplo de Salida

```plaintext
Comprador1 tiene un presupuesto de 50
Vendedor1 ofrece el artículo por 35
Comprador1 compra el artículo por 35

Comprador1 tiene un presupuesto de 15
Vendedor1 ofrece el artículo por 40
Comprador1 no puede comprar el artículo, precio: 40, presupuesto: 15

Comprador1 tiene un presupuesto de 15
Vendedor1 ofrece el artículo por 30
Comprador1 no puede comprar el artículo, precio: 30, presupuesto: 15
