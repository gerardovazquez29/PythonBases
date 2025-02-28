
# Diccionarios
# Un diccionario es una estructura de datos que permite almacenar pares clave-valor.
# Las claves son únicas y los valores pueden ser de cualquier tipo de dato.
# Los diccionarios son mutables, es decir, se pueden modificar después de haber sido creados.
# Los diccionarios se crean utilizando llaves {} y los pares clave-valor se separan por comas.
# Las claves y los valores se separan por dos puntos :.

# Crear un diccionario
diccionario = {'c1':'valor1','c2':'valor2'}
print(diccionario)
resultado = diccionario['c1']
print(resultado)

cliente = {'nombre': 'juan','apellido':'Fuentes','edad':23}
consulta = (cliente['edad'])
print(consulta)

# para imprimir la letra  en mayuscula
dic = {'c1':['a','b','c'],'c2':['d','e','f']}
print(dic['c2'][1].upper())

# agregamos 
dic1 = {1:'a',2:'b'}
print(dic1)
dic1[3] = 'c'
print(dic1)

#remplasar
dic1[2] = 'B'
print(dic1)

print(dic1.values())
print(dic1.keys())
print(dic1.items())

mi_dic = {
'nombre': 'Karen',
'apellido': 'Jurgens',
'edad': 35,
'ocupacion': 'Periodista'
}
print(mi_dic)

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])


mi_dic = {
    "nombre":"Karen", 
    "apellido":"Jurgens", 
    "edad":35, 
    "ocupacion":"Periodista"
    }
mi_dic['edad'] = 36
mi_dic['ocupacion'] = "Editora"
mi_dic["pais"] = "colombia"
print(mi_dic)

diccionario = {'c1':'valor1','c2':'valor2'}
print(diccionario)
diccionario.pop('c1')
print(diccionario)

