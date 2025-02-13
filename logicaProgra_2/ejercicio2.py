
resumen = input('Ingresa un texto a tu eleccion porfavor \r\n')
letras = input('Ingresa 3 letras a tu eleccion porfavor \r\n')


# Convertir el texto y las letras a minúsculas para evitar problemas de mayúsculas/minúsculas
resumen = resumen.lower()
letras = letras.lower()

# Contar cuántas veces aparece cada letra en el texto
# en la lista podemos contar las letras y con el ciclo for se iteran
contar_letras = {letra: resumen.count(letra) for letra in letras}
#print(contar_letras)


# Mostrar el conteo de cada letra
# con el ciclo for itera el texto para contar las letras 
for letra, conteo in contar_letras.items():
    if conteo == 1:
        veses = 'vez'
    else:
        veses = 'veces' 
    print(f'la letra {letra} aparece {conteo} {veses} en el texto. ')


# Contar la cantidad de palabras en el texto
# el metodo split divide la cadena de texto
# el metodo len cuenta las letras
palabras = resumen.split()
#print(palabras)
cantidad_palabras = len(palabras)
print(f'El texto tiene {cantidad_palabras} palabras.')

# Mostrar la primera y última letra del texto
primera_letra = resumen[0]
ultima_letra = resumen[-1]
print(f'La primera letra del texto es: "{primera_letra}" y la ultima letra es: "{ultima_letra}".')


# Mostrar el texto en orden inverso
texto_inverso = resumen[::-1]
print(f"El texto invertido es: '{texto_inverso}'.")


# Verificar si la palabra 'python' está en el texto
contiene_python =  "python" in resumen
dic = {True: 'si', False: 'no'}
print(f'La palabra "pytho": {dic[contiene_python]} se encuentra en el texto .') 
