
'''
Escribe una función llamada contar_primos() que requiera un solo argumento numérico.
Esta función va a mostrar en pantalla todos los números primos existentes 
en el rango que va desde cero hasta ese número incluido, 
y va a devolver la cantidad de números primos que encontró.
Aclaración, 
por convención el 0 y el 1 no se consideran primos.
'''

# Función para determinar si un número es primo
def es_primo(n):
#Si el número es menor o igual a 1, no es primo
    if n <= 1:
        return False
# Verificar si el número es divisible por algún número entre 2 y la raíz cuadrada de n   
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
# Si no es divisible por ninguno de esos números, es primo
    return True

# Función para contar y mostrar los números primos hasta un número dado
def contar_primos(num):
# Contador de números primos
    primos = 0
# Iterar desde 0 hasta el número dado (inclusive)
    for i in range( num + 1):
# Si el número es primo, imprimirlo y aumentar el contador
        if es_primo(i):
            print(i)
            primos += 1
# Devolver la cantidad de números primos encontrados
    return primos
# Llamar a la función contar_primos con el número 10 y mostrar el resultado
print(contar_primos(10))



print(f"\r\n*** Ejercicio2***\r\n")


def contar_primo(numero):
# Inicializar la lista de números primos con el primer número primo conocido, que es 2
    primos = [2]
# Iniciar la iteración desde el primer número impar mayor que 2, que es 3
    iteracion = 3
# Si el número dado es menor que 2, no hay números primos en ese rango
    if numero < 2:
        return 0
# Continuar iterando mientras el número actual sea menor o igual al número dado   
    while iteracion <= numero:
# Verificar si el número actual es divisible por algún número impar menor que él      
        for n in range(3, iteracion, 2):
            if iteracion % n == 0:
 # Si es divisible, no es primo, incrementar el número actual en 2 (siguiente impar) y salir del bucle               
                iteracion += 2
                break
        else:
# Si no es divisible por ningún número impar menor que él, es primo
            primos.append(iteracion)
# Incrementar el número actual en 2 (siguiente impar)            
            iteracion += 2
# Imprimir la lista de números primos encontrados            
    print(primos)
# Devolver la cantidad de números primos encontrados    
    return len(primos)
# Llamar a la función contar_primo con el número 1 y mostrar el resultado
print(contar_primo(1))
