
palabra = "python"

lista = []
for letra in palabra:
    lista.append(letra)
print(lista)

# Otra forma de hacerlo
lista = [letra for letra in "python"]
print(lista)

lista2 = [numero for numero in range(0, 20,2)]
print(lista2)

lista3 = [numero if numero * 2 > 10 else "no" for numero in range(0, 21,2)]
print(lista3)

pies = [10, 20, 30]
metros = [pie * 3.281 for pie in pies]
print(metros)

# Ejercicios
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [valor**2 for valor in valores]
print(valores_cuadrado)


valores = [1, 2, 3, 4, 5, 6, 9.5] 
valores_pares = [valor for valor in valores if valor%2 == 0]
print(valores_pares)


temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(temperatura-32)*(5/9) for temperatura in temperatura_fahrenheit]
print(grados_celsius)


