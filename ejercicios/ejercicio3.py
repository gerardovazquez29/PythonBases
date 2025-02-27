
from random import randint
numero_secreto = randint(1, 100)
intentos = 0
numero = 0

input('Bienvenido al juego de adivinar el numero secreto, presiona enter para continuar: \r\n')

nombre = input('ingresa tu nombre: \r\n')
print(f'Hola {nombre},he pensado en un numero entre 1 y 100 \n tendras ocho intentos  para adivinarlo \r\n') 

while intentos < 8:
        numero = int(input('Ingresa un numero: \r\n'))
        intentos += 1
        if numero not in range(1, 101):
            print('El numero ingresado es incorrecto, intentalo de nuevo')
        elif numero < numero_secreto:
            print('Mi numero es mayor, intenta de nuevo')
        elif numero > numero_secreto:
            print('Mi numero es menor, intenta de nuevo')
        else:
            print(f'Felicidades {nombre} has adivinado mi numero secreto en {intentos} intentos')
            break
if  numero != numero_secreto:
    print(f'Lo siento {nombre} has agotado tus intentos, el numero secreto era {numero_secreto}')
        
    
