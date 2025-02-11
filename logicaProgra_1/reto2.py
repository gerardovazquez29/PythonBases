
preguntas = ['Eres mayor de edad? (si/no): \r\n',
              'Tienes INE? (si/no): \r\n', 
              'Tienes CURP? (si/no): \r\n']

calificacion = 0

for pregunta in preguntas:
    respuesta = input(pregunta)
    if respuesta == 'si':
        calificacion += 1
    elif respuesta == 'no':
        calificacion == 0
   

print(f' Tu calificacion es: {calificacion}')
