
class Restaurant:
    def __init__(self,nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, categoria: {self.categoria}, precio: {self.precio}')

restaurant = Restaurant('Pizzeria Mexico', 'Comida Italiana', 50)
restaurant.mostrar_informacion()

restaurant2 = Restaurant('Hamburguesas el Infierno', 'Comida Rapida', 20)
restaurant2.mostrar_informacion()