
# Tuplas
# ordenadas e inmutables
# se pueden repetir elementos
# son heterojenias
mi_tuple = (1,2,3,4,5)
print(mi_tuple)
print(mi_tuple[2])

t = (1,2,3)
a,s,d = t
print(t)

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))

print(mi_tupla.index(3))

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)
print(mi_lista)

mi_tupla = (1, 2, 3, 4)
a, b, c, d = mi_tupla
print(mi_tupla)