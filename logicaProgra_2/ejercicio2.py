
resumen = input('Ingresa un texto a tu eleccion porfavor')
letras = input('Ingresa 3 letras a tu eleccion porfavor')
"""
Ahora que ya sabes usar los métodos y las propiedades de los strings, que sabes indexar


# Convertir el texto y las letras a minúsculas para evitar problemas de mayúsculas/minúsculas
resumen = resumen.lower()
letras = letras.lower()

# Contar cuántas veces aparece cada letra en el texto
conteo_letras = {letra: resumen.count(letra) for letra in letras}

# Mostrar el conteo de cada letra
for letra, conteo in conteo_letras.items():
    print(f"La letra '{letra}' aparece {conteo} veces en el texto.")

# Contar la cantidad de palabras en el texto
palabras = resumen.split()
cantidad_palabras = len(palabras)
print(f"El texto tiene {cantidad_palabras} palabras.")

# Mostrar la primera y última letra del texto
primera_letra = resumen[0]
ultima_letra = resumen[-1]
print(f"La primera letra del texto es '{primera_letra}' y la última letra es '{ultima_letra}'.")

# Mostrar el texto en orden inverso
texto_inverso = resumen[::-1]
print(f"El texto invertido es: {texto_inverso}")

# Verificar si la palabra 'python' está en el texto
contiene_python = 'python' in resumen
print(f"El texto contiene la palabra 'python': {contiene_python}")
"""

