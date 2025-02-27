
from random import *

print('Ejercicio1 \n\r')

def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    print(f"Tus dados son: {dado1} y {dado2}")
    return dado1, dado2

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6 :
        print(f"La suma de tus dados es {suma_dados}. Lamentable")
    elif suma_dados <= 10:
        print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    else:
        print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")
evaluar_jugada(*lanzar_dados())
print('\n\r')

print('Ejercicio2 \n\r')

lista_numeros = [1,2,15,7,2,8]

def reducir_lista(lista):
    # se convierte la lista en un conjunto set para eliminar duplicados
    lista = list(set(lista))
    # se ordena la lista
    lista.sort()
    # se elimina el ultimo elemento
    lista.pop(-1)
    return lista

def promedio(lista):
    # se suma el promedio de la lista y se divide por la cantidad de elementos
    valor_medio = sum(lista)/len(lista)
    return valor_medio

lista_reducida = reducir_lista(lista_numeros)
print(f"Lista reducida es: {lista_reducida}")

promedio_lista = promedio(lista_reducida)
print(f"El promedio de la lista es: {promedio_lista}")

print('\n\r')
print('Ejercicio3 \n\r')

lista_numeros = [1,2,15,7,2,8]

def lanzar_moneda():
    return choice(["cara", "cruz"])
print(lanzar_moneda())

def probar_suerte(moneda, lista):
    if moneda == "cara":
        print("La lista se autodestruira")
        return  [ ]
    elif moneda == "cruz":
        print("La lista fue salvada")
        return lista
probar_suerte(moneda = lanzar_moneda(), lista = lista_numeros)