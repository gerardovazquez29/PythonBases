
def saludar_persona(nombre):
    '''
    Función que saluda a una persona
    '''
    print(f"Hola, ¿Cómo estás? {nombre}")

saludar_persona('Juan')

un_numero = 5

def cuadrado(un_numero):
    print(un_numero**2)
cuadrado(5)

def multiplicar(num1, num2):
    return num1 * num2
resultado = multiplicar(5, 6)
print(resultado)

def potencia(num1, num2):
    return num1 **num2
resultado = potencia(2, 3)
print(resultado)

dolares = 10
def usd_a_eur(dolares):
    total =  dolares * 0.90
    return total
usd_a_eur(dolares)
print(usd_a_eur)


# 
palabra = "Hola"
def invertir_palabra(palabra):
    return palabra[::-1].upper()
print(invertir_palabra(palabra))


def chequear_3_cifras(numero):
    return numero in range(100, 1000)
resultado = chequear_3_cifras(564)
print(resultado)


def checa_cifras(lista):
    lista_cifras = []
    for n in lista:
        if n in range(100, 1000):
            lista_cifras.append(n)
        else:
            pass
    return lista_cifras
resultado2 = checa_cifras([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 200, 300,])
print(resultado2)



def todos_positivos(lista):

    for n in lista:
        if n < 0:
            return False
        else:
            pass
    return True
resultado3 = todos_positivos([1, 2, -3, 4, 5, 6, 7, 8, -9, -10])
print(resultado3)



lista_numeros =[55, 44, 33, 22, 11,352,548]

def suma_menores(lista_numeros):
    suma = 0
    for numeros in lista_numeros:
        if numeros in range(1, 1000):
            suma += numeros
        else:
            pass
    return suma
resultado4 = suma_menores(lista_numeros)
print(resultado4)



lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def cantidad_pares(lista_numeros):
    cantidad = 0
    for numeros in lista_numeros:
        if numeros % 2 == 0:
            cantidad += 1
        else:
            pass
    return cantidad
resultado5 = cantidad_pares(lista_numeros)
print(resultado5)

