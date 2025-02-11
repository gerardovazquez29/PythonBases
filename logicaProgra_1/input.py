
# el input sirve para pedir datos al usuario
nombre = input('Cuál es tu nombre: \r\n ') # \r\n es un salto de línea
print(f'Hola {nombre}')


#leer datos que seran numeros
edad = input('Cual es tu edad:')
#convertir a entero
edad = int(edad)
if edad >= 18:
  print('Eres mayor de edad')
else:
    print('Eres menor de edad')
    print(f'tu edad es {edad} años')


