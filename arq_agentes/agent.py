import random

# Clase base
class Agent:
    def __init__(self, name):
        self.name = name

    def act(self):
        pass

# Agente Comprador
class BuyerAgent(Agent):
    def __init__(self, name, budget):
        super().__init__(name)
        self.budget = budget

    def act(self, seller):
        print(f"{self.name} tiene un presupuesto de {self.budget}")
        price = seller.offer_price()
        if self.budget >= price:
            print(f"{self.name} compra el artículo por {price}")
            self.budget -= price
        else:
            print(f"{self.name} no puede comprar el artículo, precio: {price}, presupuesto: {self.budget}")

# Agente Vendedor
class SellerAgent(Agent):
    def __init__(self, name, min_price):
        super().__init__(name)
        self.min_price = min_price

    def offer_price(self):
        price = random.randint(self.min_price, self.min_price + 20)
        print(f"{self.name} ofrece el artículo por {price}")
        return price

# Ejecución de la simulación
buyer = BuyerAgent("Comprador1", 50)
seller = SellerAgent("Vendedor1", 30)

for _ in range(3):  # Tres intentos de compra
    buyer.act(seller)
    print()


