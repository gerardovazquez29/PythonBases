
def informacion():
    print("Este es un mensaje de la función informacion")

informacion()

# funciones con parámetros y argumentos

def informacion(nombre, puesto):
    print(f'Soy {nombre} y soy {puesto}')

informacion('Luis', 'Desarollador')
informacion('Juan','Diseñador')
informacion('Pedro','Ingeniero')

# funciones con retorno

def info(nombre):
    return nombre

empleado= info('Luis')
print(empleado)

# funciones con retorno y parámetros

def mostrar_nombre(nombre):
    return f'Mi nombre es {nombre}'
nombre= mostrar_nombre('Luis')
print(nombre)

# metodo
print(nombre.upper())


def saludo(mensaje):
    print(mensaje)

saludo("Hola ")


def despedida(mensaje2):
    return f"Adios {mensaje2}"
print(despedida("Luis"))

