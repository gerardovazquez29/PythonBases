
class Restaurant:
        # metodo
        def agregar_restaurant(self, nombre):
            self.nombre = nombre # atributo

        def mostrar_informacion(self):
              print(f'Nombre: {self.nombre}')


# Instanciar la clase
restaurant = Restaurant()
restaurant.agregar_restaurant('Pizzeria Mexico')
restaurant.mostrar_informacion()

restaurant2 = Restaurant()
restaurant2.agregar_restaurant('Hamburguesas Pepito')       
restaurant2.mostrar_informacion()

# Mostrar Informacion
print(f'Nombre del Restaurante: {restaurant.nombre}')
print(f'Nombre del Restaurante: {restaurant2.nombre}')