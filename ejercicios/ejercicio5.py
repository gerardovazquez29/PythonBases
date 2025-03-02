
'''
Crea una función llamada devolver_distintos() que reciba 3integers
como parámetros, Si la suma de los 3 numeros es mayor a 15 , va a
devolver elnúmero mayor . Si la suma de los 3 numeros es menor a 10
va a devolver elnúmero menor
Si la suma de los 3 números es un valor entre 10 y 15(incluidos)
va a devolver el número de valor intermedio
'''

def devolver_distintos(args):
# Verifica que la lista contenga exactamente 3 números
    if len(args) != 3:
        raise ValueError('la lista debe contener 3 numeros')
# Calcula la suma de los números en la lista   
    total = sum(args)

# Si la suma es mayor que 15, devuelve el número mayor de la lista   
    if total > 15:
        return max(args)
# Si la suma está entre 10 y 15 (inclusive), devuelve el número del medio en la lista ordenada    
    elif 10 <= total <= 15:
        return sorted(args)[1]
 # Si la suma es menor que 10, devuelve el número menor de la lista   
    else:
        return min(args)
# Llama a la función con una lista de 3 números y almacena el resultado    
resultado = devolver_distintos([6, 4, 2])
print(resultado)