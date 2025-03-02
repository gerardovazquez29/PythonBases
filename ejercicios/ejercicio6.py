
'''
Escribe una función
(puedes ponerle cualquier nombre que quieras)
que reciba cualquier palabra como parámetro, y que devuelva todas sus letras únicas
(sin repetir)
pero en orden alfabético.
Por ejemplo si al invocar esta función pasamos la palabra"entretenido", 
debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']
'''

# el metodo sorted()

def orden_palabras(args):
    i = []
    for i in args:
# ordena cualquier iterable como listas, tuplas y devuelve una nueva lista
        return sorted(set(args))
print(orden_palabras('funcion'))
    