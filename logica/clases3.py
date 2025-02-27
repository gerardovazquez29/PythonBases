

class Restaurant:
    def __init__(self,nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.__precio = precio  
        # Default: Public, PROTECTED _ = es protected y __ = es Private
        
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, categoria: {self.categoria}, precio: {self.__precio}')

    # GETTERS Y SETTERS - Get = Obtiene un valor, SET = Agrega un valor
    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio


restaurant = Restaurant('Pizzeria Mexico', 'Comida Italiana', 50)
#restaurant.__precio = 80  # No sera posible modificarlo con Private __
restaurant.mostrar_informacion()
restaurant.set_precio(80)
precio = restaurant.get_precio()
print(precio)

restaurant2 = Restaurant('Hamburguesas el Infierno', 'Comida Rapida', 20)
restaurant2.mostrar_informacion()
restaurant2.set_precio(30)
restaurant2.get_precio()