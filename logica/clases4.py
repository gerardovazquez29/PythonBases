
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

# Crear una clase hijo de Restaurant

class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio):
        super().__init__(nombre, categoria, precio)

hotel = Hotel('Hotel POO', '5 Estrellas', 200) 
hotel.mostrar_informacion()
