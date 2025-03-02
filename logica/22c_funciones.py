
# (*args) = argumentos variables
# Se pueden pasar varios argumentos a una función
# y se pueden pasar tantos como se quiera   
# Se pueden pasar como una tupla


def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(suma(5, 6,9))


# ejemplo

def suma(*args):
    return sum(args)
print(suma(7, 9, 25, 62))

print(f"\r\n*** Ejercicio1***\r\n")

def suma_cuadrados(*args):
    total = 0
    for suma in args:
        total += suma**2
    return total
print(suma_cuadrados(1,2,3))


print(f"\r\n*** Ejercicio2***\r\n")

def suma_absolutos(*args):
    total = 0
    for arg in args:
        total += abs(arg)
    return total
print(suma_absolutos(-5, 6, -7, 4))

print(f"\r\n*** Ejercicio3***\r\n")

def numeros_persona(*args):
    nombre = 'jose'
    suma_numeros = 0
    for suma_numero in args:
        suma_numeros += suma_numero
    return nombre, suma_numeros
nombre, suma_numeros = numeros_persona(5, 6, 4)
print(f"{nombre}, la suma de tus números es {suma_numeros}")


# **kwargs = argumentos variables
# Se pueden pasar varios argumentos a una función       
# y se pueden pasar tantos como se quiera
# Se pueden pasar como un diccionario

def suma(**kwargs):
    print(type(kwargs))
suma(a=5, b=6, c=7)

def suma(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total
print(suma(a=5, b=6, c=7))


def prueba(num1, num2, *args, **kwargs):
    print(f'el primer valor es {num1}')
    print(f'el segundo valor es {num2}')
    for arg in args:
        print(f'argumento = {arg}')
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

args = [1, 2, 3, 4, 5]
kwargs = {'a': 6, 'b': 7, 'c': 8}
prueba(5, 6, *args, **kwargs)

print(f"\r\n*** Ejercicio4***\r\n")

def lista_atributos(**kwargs):
    lista = []
    for valor in kwargs.values():
        lista.append(valor)
    return lista
print(lista_atributos(a=5, b=6, c=7))


print(f"\r\n*** Ejercicio5***\r\n")

def describir_persona(nombre, **kwargs):
# Imprime el nombre de la persona
    print(f'Cararcteristicas de {nombre}')
# Itera sobre los argumentos adicionales (kwargs) y los imprime
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')
# Llama a la función describir_persona con el nombre 'Jose' y varios atributos adicionales  
describir_persona('Jose', edad=20, estatura=1.70, peso= 70)
