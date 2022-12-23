#1. dado el siguiente diccionario:

diccionario = {
    "clase": {
        "alumno": {
            "nombre": "Carlos Peña",
            "cursos": {
                "Historia": 17,
                "Ciencias": 15
            }
        }
    }
}

#Escribir el código para acceder a la nota de ciencias y mostrarla en pantalla
print("Pregunta 1:")
print("Nota de ciencias:")
print(diccionario["clase"]["alumno"]["cursos"]["Ciencias"])

#######################################################################################


#2. Dado el siguiente diccionario:

diccionario_2 = {
    "nombre": "María",
    "edad": 25,
    "salario": 8000,
    "ciudad": "New york"
}

#y las claves:
claves = ["nombre", "salario"]

#Implementar una función que reciba como parámetros el diccionario y la lista claves
#y retorne un nuevo diccionario conteniendo solo las claves de la lista y sus valores:

#{'nombre': 'María', 'salario': 8000}

print("Pregunta 2:")
def funcion2(dic,keys):
    r={}
    for key in keys:
        r[key]=dic[key]
    return r

print(funcion2(diccionario_2,claves))    


#######################################################################################

#3. Dada la lista y diccionario siguientes:

empleados = ['Marcelo', 'Juan']
asignación = {"cargo": 'Analista', "salario": 8000}

#Implementar una función que reciba como parámetros la lista de empleados y la asignación y retorne
#un diccionario cómo en el ejemplo:

#{'Marcelo': {"cargo": 'Analista', "salario": 8000}, 'Juan': {"cargo": 'Analista', "salario": 8000}}
print("Pregunta 3:")
def function3(dis,lista):
    r={}
    for l in lista:
        r[l]=dis
    return r

print(function3(asignación,empleados))

#######################################################################################

# 4. Dado el siguiente diccionario

diccionario_3 = {
    "nombre": "María",
    "edad": 35,
    "salario": 2500,
    "ciudad": "Tokio"
}

#Implementar un código que permita modificar la clave "ciudad" por "locación"
print("Pregunta 4:")
diccionario_3["locación"]=diccionario_3["ciudad"]
del diccionario_3["locación"]
print(diccionario_3)

#######################################################################################

#5. En el siguiente diccionario se ha registrado de forma errónea el salario del usuario 3, el valor es 5000

diccionario_4 = {
    'Usuario1': {'nombre': 'Karina', 'salario': 4500},
    'Usuario2': {'nombre': 'Martin', 'salario': 8000},
    'Usuario3': {'nombre': 'Rudolph', 'salario': 500}
}

#Se le solicita escribir el código para corregir el salario del Usuario3
print("Pregunta 5:")
diccionario_4["Usuario3"]["salario"]=5000

print(diccionario_4)

#######################################################################################

#6. Crear una tupla con 30 números aleatorios entre 50 y 100
print("Pregunta 6:")

import random
x=[]
for i in range(30):
    n = random.randint(50 , 100)    
    x.append(n)
x=tuple(x)
print(x)

#######################################################################################

#7. Dada la siguiente tupla

tupla = (('w', 215), ('x', 491), ('y', 180), ('z', 345))

#Se requiere escribir un código para ordenar la tupla en función al segundo elemento de las tuplas pares. 
#La salida debe ser: (('c', 180), ('a', 215), ('d', 345), ('b', 491))
print("Pregunta 7:")
array = []
for t in tupla:
    array.append(t)
for i in range(len(array)):
    for j in range(len(array)-1): 
        if( array[j+1][1]  < array[j][1] ):
            aux=array[j]
            array[j]=array[j+1]
            array[j+1]=aux
tupla=tuple(array)
print(tupla)            



     
#######################################################################################

#8. Dada la siguiente tupla:

Tupla = (10, 20, 30, 40, 50, 60, 70, 80)

#Escriba el código que da como resultado: (30, 40, 50) (10, 20, 30, 40) (40, 50, 60, 70, 80)
print("Pregunta 8:")
print(Tupla[2:5])
print(Tupla[:4])
print(Tupla[3:])