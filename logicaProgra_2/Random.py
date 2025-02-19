
from random import *

aleatorio = randint(1,5)
print(aleatorio)

aleatorio1 = round(uniform(1,5),1)
print(aleatorio1)

aleatorio2 = random()
print(aleatorio2)

colores = ["rojo", "azul", "verde", "amarillo"]
aleatorio3 = choice(colores)
print(aleatorio3)

numeros = list(range(1,11,2))
shuffle(numeros)
print(numeros)

