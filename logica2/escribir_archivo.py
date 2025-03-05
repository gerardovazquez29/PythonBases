
archivo = open('prueba.txt', 'a') # con a escribes al final de la linea
                                  # con w sobreescribes el contenido
# archivo.write('soy el nuevo texto')

'''
lista = ['hola', 'mundo', 'aqui', 'estoy']

for p in lista:
    archivo.writelines(p + '\n')
'''

archivo.write('bienvenido')

archivo.close()


registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
 
registro = open("registro.txt","a")
for item in registro_ultima_sesion:
    registro.writelines(item +'\t')
 
registro.close()
registro = open("registro.txt","r")
print(registro.read())