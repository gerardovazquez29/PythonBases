
mensaje = input("Ingresa un texto a tu preferencia:\n\r").lower()
print( "Ingresa 3 Letras porfavor")
letra_1 = input("ingresa la primera letra\n\r").lower()
letra_2 = input("ingresa la segunda letra\n\r").lower()
letra_3 = input("ingresa la tercer letra\n\r").lower()

letras = [letra_1, letra_2, letra_3]

for palabra in letras:
    conteo = mensaje.count(palabra)
    if conteo == 1 :
        veses = "vez"
    else:
        veses = "veses"
    print(f"la palabra: {palabra} aparece {conteo} {veses} en el mensaje ")

palabras = mensaje.split()
conteo_palabras = len(palabras)
print(f" El mensaje tiene {conteo_palabras} palabras ")

if len(mensaje) > 0:
    primera_letra = mensaje[0]
    ultima_letra = mensaje[-1]
    print(f"la primera letra del mensaje es: {primera_letra} y la ultima letra es : {ultima_letra}")
    mensaje_invertido = mensaje[::-1]
    print(f"El mensaje invertido es: {mensaje_invertido}")
else:
    print("No hay mensaje")

'''
palabra_a_buscar = input("Ingresa una palabra para verificar si aparece en el mensaje \r\n")
palabra_a_buscar = mensaje.count(palabra)
letras_mensaje = list(mensaje)

if palabra_a_buscar in letras_mensaje:
    print(f"la palabra '{palabra_a_buscar}' aparese en el mensaje")
else:
    print(f"la palabra '{palabra_a_buscar}' no aparese en el mensaje")
'''
'''
for palabra in mensaje:
        palabra_a_buscar in mensaje
        dic = {True: 'si', False: 'no'}
        print(f'La palabra {palabra_a_buscar}: {dic[palabra]} se encuentra en el texto .') 
    '''
