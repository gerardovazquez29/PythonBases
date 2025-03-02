
'''
Escribe una función que requiera una cantidad indefinida de argumentos. 
Lo que hará esta función es devolver True
si en algún momento se ha ingresado al numero cero
repetido dos veces consecutivas
.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False
'''

def numeros(args):
#Itera a través de los elementos de 'args' hasta el penúltimo elemento   
    for i in range(len(args) -1):
#Verifica si el elemento actual y el siguiente son ambos cero       
        if args[i] == 0 and args[i + 1] == 0:
#Si se encuentran dos ceros consecutivos, devuelve True           
            return True
#Si no se encuentran dos ceros consecutivos, devuelve False       
    return False
    
print(numeros([5, 6, 1, 0, 0, 9, 3, 5]))
print(numeros([6, 0, 5, 1, 0, 3, 0, 1])) 