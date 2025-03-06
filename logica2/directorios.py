
import os
'''
ruta = os.chdir('C:\\Users\\T-City\\OneDrive\\Documentos\\documento.txt')

archivo = open('documento.txt', 'r')

print(archivo)


'''
'''
ruta = 'C:\\Users\\T-City\\OneDrive\\Documentos\\documento.txt'

with open(ruta, 'r') as archivo:
    contenido = archivo.read()

print(contenido)
'''



from pathlib import Path

archivo = Path('C:/Users/T-City/OneDrive/Documentos/documento.txt')

with open(archivo, 'r') as archivo:
    contenido = archivo.read()

print(contenido)
