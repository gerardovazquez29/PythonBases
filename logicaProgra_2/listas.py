
mi_lista = ["a", "b", "c"]
mi_lista2 = ["e","f","g"]
resultado = len(mi_lista2)
print(resultado)

medios_transporte = ["avión", "auto", "barco", "bicicleta"]
# Agregar un elemento al final de la lista
medios_transporte.append("motocicleta")
print(medios_transporte)


frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
# Eliminar un elemento de la lista
eliminado = frutas.pop(2)
print(frutas)
print(eliminado)


frutas = ["manzana", "banana", "mango", "cereza", "sandía", "banana",]
#contar cuantas veces se repite un elemento en la lista
print(frutas.count("banana"))
#obtener el indice de un elemento en la lista
print(frutas.index("manzana"))
#eliminar un elemento de la lista
print(frutas.remove("banana"))