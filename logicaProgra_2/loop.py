
#for

lista = [1,2,3,4,5,6,7,8,9,10]

for num in lista:
    numero_num = lista.index(num) + 1	
    print(f'El numero {num} esta en la posicion {numero_num}')


lista = ['pablo', 'juan', 'pedro', 'maria', 'luisa']

for nombre in lista:
    if nombre.startswith('m'):
        print(nombre)

numeros = [1,2,3,4,5]
mi_valor = 0
for numero in numeros:
    mi_valor += numero
print(mi_valor)


alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for alumno in alumnos_clase:
    print(f"Hola {alumno}")

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for suma_numero in lista_numeros:
    suma_numeros += suma_numero
print(suma_numeros)

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares += numero   
    else:
        suma_impares += numero    
print(suma_pares)
print(suma_impares)

#while
monedas = 5
while monedas >= 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("No tengo más monedas")


numero = 10

while numero >= 0:
    print(numero)
    numero -= 1


numero = 50
while numero >= 0:
    if numero % 5 == 0:
        print(numero)
        numero -= 1
    else:
        numero -= 1

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for numero in lista_numeros:
    if numero < 0:
        print(f"El número {numero} es negativo")
        break
    else:
        print(numero)

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
 
for numero in lista_numeros:
    if numero >= 0:
        print(numero)
    else:
        break


for numero in range(0,10,2):
    print(numero)

lista = list(range(1, 101))
print(lista)

suma_cuadrtados = 0
for numero in range(1,16):
    suma_cuadrtados += numero**2
print(suma_cuadrtados)

lista = ['a', 'b', 'c', 'd',]
for item in enumerate(lista):
    print(item)

for indice in enumerate(range(10,20)):
    print(indice)

lista = ['a', 'b', 'c']
mi_valor = list(enumerate(lista))
print(mi_valor)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

lista_indices = list(enumerate("Python"))
print(lista_indices)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice, nombre in enumerate(lista_nombres):
   if nombre[0] == "M":
    print(indice, nombre)

nombres = ["Marcos", "Laura", "Mónica"]
edades = [25, 30, 35]
ciudades = ["Buenos Aires", "Córdoba", "Rosario"]
combinados = list(zip(nombres, edades, ciudades))
print(combinados)
for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}") 

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
combos = list(zip(capitales, paises))
for capital, pais in combos:
    print(f"la capital de {pais} es {capital}")

marcas = ["Nike", "Lenovo", "Nissan"]
productos = ["zapatillas", "notebook", "automóviles"]
 
mi_zip = zip(marcas, productos)
print(list(mi_zip))


espaniol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]
 
numeros = list(zip(espaniol, portugues, ingles))
print(numeros)

lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo = max(lista_numeros)
print(valor_maximo)

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
rango = max(lista_numeros) - min(lista_numeros)
print(rango)    


diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())
print(edad_minima)
print(ultimo_nombre)
