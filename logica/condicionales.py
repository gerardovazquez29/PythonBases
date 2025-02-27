#Revisar si una condicion es mayor a

balance = 0
if balance > 0:
    print("Usted tiene saldo disponible")
else:
    print("Usted no tiene saldo disponible")

# Revisar si hay likes
likes = 200
if likes >= 200:
    print("Excelente, tienes 200 likes")
else:
    print("Necesitas mas likes")


#if con texto
lenguaje = "Python"
if lenguaje == "Python":
    print("Excelente, Python es un lenguaje de programacion")


# if con negacion
lenguaje = "php"
# not es una negacion de la condicion es decir si no es igual a python
if not lenguaje == "python": 
    print("Excelente decicion")

# if con boleanos

usuario_autenticado = True

if usuario_autenticado:
    print("Usuario autenticado")
else:
    print("Usuario no autenticado")


# evaluar un elemento de una lista

lenguajes = ['Python', 'Java', 'Ruby', 'JavaScript' , 'php']
if 'php' in lenguajes:
    print("php si existe")
else:
    print("php no existe")

# if anidados

usuario_autenticado = True
usuario_admin = True

if usuario_autenticado:
    if usuario_admin:
        print('Acceso total')
    else:
        print('Acceso al sistema')
else:
    print('Acceso denegado')

# elif
# elif es una condicion que se evalua si la condicion anterior no se cumple

ocupacion = 'Estudiante'

if ocupacion == 'Estudiante':
    print('Tienes 50% de descuento')
elif ocupacion == 'Jubilado':
    print('Tienes 75% de descuento')
elif ocupacion == 'Desempleado':
    print('Tienes 10% de descuento')
else:
     print('Debes pagar el precio completo')

# if con operadores logicos
# and, or, not

usuario_logueado = True
usuario_admin = True

if usuario_logueado and usuario_admin:
    print('Administrador')
elif usuario_logueado:
    print('Acceso al sistema')
else:
    print('Debes iniciar sesion')


