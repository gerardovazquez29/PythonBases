
archivo = open('prueba.txt', 'r')
#contenido = archivo.read()
'''
contenido = archivo.readline()
print(contenido)

contenido = archivo.readline()
print(contenido)

contenido = archivo.readline()
print(contenido)
'''

'''
for l in archivo:
    print(f"Aqui dice: {l}")
'''
todos = archivo.readlines()
print(todos)            # devuelve una lista

archivo.close()