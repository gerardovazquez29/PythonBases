
playlist = {} # diccionario vacio
playlist['canciones'] = [] # lista vacia

# funcion principal
def app():
    #agregar playlist
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input('Como deseas nombrar la playlist? \r\n')
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist

            #  ya tenemos el nombre de la playlist
            agregar_playlist = False
            
            # Mandar a llamar la funcion para agregar canciones
            agregar_canciones()
def agregar_canciones():
    agregar_cancion = True

    while agregar_cancion:
        # preguntar al usuario por una cancion a agregar
        nombre_playlist = playlist['nombre']
        pregunta = f'\r\n Agrega canciones para la playlist {nombre_playlist}: \r\n'
        pregunta += 'Escribe "X" para dejar de agregar canciones \r\n'

        cancion = input(pregunta)
        if cancion == 'x':
            # Dejar de agregar canciones
            agregar_cancion = False 
            # Mostrar resumen de la playlist
            mostrar_resumen()       
        else:
            # agregar cancion a la playlist
            playlist['canciones'].append(cancion)
def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'Playlist: {nombre_playlist} \r\n')
    print('Canciones: \r\n')
    for cancion in playlist['canciones']:
        print(cancion)
app()