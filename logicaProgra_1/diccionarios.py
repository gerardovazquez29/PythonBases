
# diccionarios en python o objetos en javascript

# diccionario vacio
jugador = {}
print(jugador)

#agregar elementos al diccionario
jugador['nombre'] = 'Juan'
jugador['puntaje'] = 0
print(jugador)

#incrementando el puntaje
jugador['puntaje'] = 100
print(jugador)

#acceder a un valor
print(jugador.get('consola', 'No existe esa llave'))


# iterar en el diccionario
for llave, valor in jugador.items():
    print(llave)
    print(valor)


# diccionario con elementos

cancion = {
    # llave   :   valor
    'artista' : 'Metalica',
    'cancion' : 'Enter Sandman',
    'lanzamiento' : 1992,
    'likes' : 3000
}
# acceder a los elementos del diccionario
print(cancion['artista'])

# mezclar con un string
print(f'estoy escuchando a {cancion['artista']} - {cancion["cancion"]}')

# almacenar los elementos a una variable
artista = cancion['artista']
print(f'estoy escuchando a {artista}')

# agregar nuevos valores
cancion['playlist'] = 'Heavy Metal'
print(cancion)

# reemplazar valor existente
cancion['cancion'] = 'Seek and Destroy'
print(cancion)

# eliminar un valor
del cancion['lanzamiento']
print(cancion)

