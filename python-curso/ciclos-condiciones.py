#CICLOS Y CONDICIONES 

#switch se agrego en las utimas versiones de python

dic = {"nombre":"lalo", "edad":40}

""" 

if dic["edad"] > 35:
    print('viejo')
elif dic["edad"] > 25 or dic["edad"] < 35: 
    print('jovenazo')
else:
    print('no tan viejo') 

"""


#operacion ternaria donde se agraga un valor desde el inicio
#si la operacion se cumple de lo contrario se agrega otro valor

variable = 'jovenazo' if dic['edad'] < 35 else 'viejito'
print(variable)


#ciclo while 

var = 5
while (var < 10):
    print(var)
    var +=1
    
#otra forma de generar la condicion
print('\nrompiendo la condicion por dentro')    

var1 = 5
while (True):
    print(var1)
    var1 +=1
    if var1 > 10:
        break 