var1 = 3
PI = 3.141592

#comentario de una sola linea
#linea 1
#linea 2
#se utiliza para comentar el codigo  
#y los econtramos en casi cualquier parte del mismo



"""
comentarios multilinea y se utilizan 
al teminar una clase o una funcion
es parte de la documentacion del codigo
"""

#TIPOS DE DATOS

var1 = 3
var2 = 2.0
var3, var4 = False, True
var5 = '3.4'
var6 = [] # o tambien como list()
var7 = {} # o tambien como dict()


#OPERADORES LOGICOS
 
True == 1
True == 0
True > False
True < False
True is False
True is not False

lista = [1,2,3,4,5]
3 in lista

""" 
LISTA
No es necesario declarar el tipo de dato de la lista
Incluso puede ser de diferentes tipos
para saber que funciones usar en un elemnto
usamos dir
ejemplo:     dir(lista)
 """

lista = [1, False, 3.4, 'cadena']
lista[2] = 5.5

#agregar elemento nuevo al final de la lista -append('elemento nuevo')-
lista.append('elemento nuevo')

#ordenar lista se utiliza sort
lista [5,7,9,1,2,4,9,2,3]
lista.sort()
lista           #se imprime la lista ordenada 

""" 
En python no existe las matricez o arreglos 
las matrices son al final listas con mas listas adentro 
y en python asi las podemos crear:
    matriz = [[3,3,3],[3,3,3],[3,3,3]]
"""

matrix = [[3,3,3],[3,3,3],[3,3,3]]
matrix      #esto imprime la matriz

#TUPLA
""" 
    es muy parecida a las lista 
    a diferencia de las listas las tuplas contine ya 
    valor fijo establecido y no se pueden cambiar ni 
    agregar mas elementos 
    es como una costante pero en lista
    se declaran con "( )" en lugar de []
 """

t = (3,"Hola",False)
print type(t)          #imprime el tipo de dato unicamente
print t
print t[1]

listaNew = list(t)     #cambiar de tupla a lista para poder modificarla
print type(listaNew)


#CADENA / STRING

var = 'variable 1'
var = '''cadena multilinea'''
var

var [-1]  #mostramos el ultimo dato de la lista o cadena

var [::-1] #imprime la cadena de inicio a fin invertida empezando desde el ultimo dato
var [:5]  # imprime hasta la linea 5

for car in range(0,len(var)):
    print(car)


var[3] = 'f'

cadena2 = var[0:3] + 'f' + var[4:]
cadena2 

numero=4
'el numero vale: '+str(numero) #forma correcta de concatenar algo que son de diferente tipo

'el numero vale: '+ numero  #marca error

'el numero vale: '+str(numero)

for car in range((len(var)-1),0,-1):
    print(var[car])

#para cambiar un valor dentro de una cadena

cadena2 = var[0:3] + 'f' + var[4:]

numero = 4
'el numero vale: ' + numero #ERROR no es la forma correcta de concatenar 
'el numero vale: ' + str(numero)

#otra forma de hacerlo es con las f strings || f'texto muestra: {variable}' 
f'el numero vale: {numero}'
f'el numero vale: {numero} y es de tipo {type(numero)}'



