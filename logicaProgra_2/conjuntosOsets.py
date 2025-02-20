
# Conjuntos
# Un conjunto es una colección de elementos sin orden, sin índices y sin elementos repetidos.
# Los conjuntos se utilizan para almacenar múltiples elementos en una sola variable.
# son mutables y no se repiten los elementos.
# Los elementos del conjunto son escritos entre llaves {} y separados por comas y utilisan el metodo set.

# Crear un conjunto
conjunto = {"manzana", "banana", "cereza"}
print(conjunto)

conjunto = set(("manzana", "banana", "cereza", "manzana"))
print(conjunto)

mi_set = set([1,2,3,4,5])
print(mi_set)
print(len(mi_set))

otro_set = {1,2,3}
print(otro_set)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

s1.add(4)
print(s1)

s1.remove(4)
print(s1)

mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)
print(mi_set_3)

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.pop()
print(sorteo)

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")
print(sorteo)

conjunto_1 = set([1, 2, 3])
conjunto_2 = set([3, 4, 5])
conjunto_3 = set([5, 6, 7])
print(conjunto_1.intersection(conjunto_2))
print(conjunto_1, conjunto_2, conjunto_3)


