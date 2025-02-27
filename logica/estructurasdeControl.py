
num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))
'''''
f"{num1} es mayor que {num2}"
"num2 es mayor que num1"
"num1 y num2 son iguales"
'''
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 == num1:
        print(f"{num2} y {num1} son iguales")
else:
    print(f"{num2} es mayor que {num1}")

#Ejercicio 2
edad = 16
tiene_licencia = False

"Puedes conducir"

"No puedes conducir aún. Debes tener 18 años y contar con una licencia"

"No puedes conducir. Necesitas contar con una licencia"

if edad >= 18 and tiene_licencia:
    print("Puedes conducir")
elif edad < 18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")  
else:
    print("No puedes conducir. Necesitas contar con una licencia")

#Ejercicio 3
habla_ingles = True
sabe_python = False

"Cumples con los requisitos para postularte"

"Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"

"Para postularte, necesitas tener conocimientos de inglés"

"Para postularte, necesitas saber programar en Python"

if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte") 
elif habla_ingles:
    print("Para postularte, necesitas saber programar en Python")       
elif sabe_python:
    print("Para postularte, necesitas tener conocimientos de inglés")
else:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")

