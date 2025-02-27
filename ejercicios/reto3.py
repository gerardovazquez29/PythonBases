
pregunta = 'Agrega un numero y te dire si es par o inpar: \r\n'
pregunta += 'Escribe "cerrar" para terminar el programa \r\n'
preguntar = True


while preguntar:
    numero = input(pregunta)

    if numero == 'cerrar':
        preguntar = False
    else:
        numero = int(numero)

        if numero % 2 == 0:
            print(f'El numero {numero} es par')
        else:
            print(f'El numero {numero} es inpar')
print('Fin del programa')
