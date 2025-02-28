#index()
# el index se utiliza para saber la posision de un elemento
mi_texto = "esta es una prueba"
resultado = mi_texto.index("")
print(resultado)
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.index("práctica"))
# el metodo rindex funciona al reves
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.rindex("práctica"))

frase = "Controlar la complejidad es la esencia de la programación"
print(frase[:9])
# funciona para imprimir el texto al reves
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
print(frase[8::3])

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza" 
print(frase[::-1])

frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
print(frase.upper())

lista_palabras = ["La","legibilidad","cuenta."]
frase = " ".join(lista_palabras)
print(frase)

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
print(frase.replace("difícil", "fácil").replace("mala","buena"))

haiku = '''
Tierra mojada
mis recuerdos de viaje,
entre las lluvias
'''
print("agua" not in haiku)

palabra = "electroencefalografista"
print(len(palabra))