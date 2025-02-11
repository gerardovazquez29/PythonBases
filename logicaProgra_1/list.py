lenguajes = ['Python', 'C', 'C++', 'Java', 'JavaScript']

print(lenguajes)

# los Arrays (lists) en Python comienzan en 0
# Acceder a un elemento de la lista
print(lenguajes[0]) # Python

# sort() ordena la lista
lenguajes.sort()
print(lenguajes)

# Acceder a un e3lemento dentro de un texto
aprendiendo = f'Estoy aprendiendo {lenguajes[4]}'
print(aprendiendo)

# Modificar un elemento de la lista
lenguajes[2] = 'PHP'
print(lenguajes)

# Agregar un elemento a la lista
lenguajes.append('Ruby')
print(lenguajes)

# Eliminar un elemento de la lista
del lenguajes[1]
print(lenguajes)

# Eliminar el último elemento de la lista
lenguajes.pop()
print(lenguajes)

# Eliminar un elemento de la lista por su valor utilizando pop()
lenguajes.pop(0)
print(lenguajes)

# Eliminar un elemento de la lista por su valor utilizando remove()
lenguajes.remove('PHP')
print(lenguajes)
