#FUNCIONES  def
# -> def <-    es la palabra rerservada para declarar las funciones 

def suma():         #se declara pero no se ejecuta hasta que se llame
    return 2+1

suma()  #asi se llama a la funcion para que se ejecute

print(suma())

#pasando valores a una funcion
x = 19     #esta es una variable global ya que esta fuera de la funcion

def suma2(x,y):
    return x+y    #son variables locales dentro de la funcion

print(suma2(6,4))

def imprimir():
    print('hola mundo')

imprimir()

def imp(cadena):
    print(f'la suma es: {cadena}')
    global x     #se usa la palabra reservada global para usar una variable global dentro de una funcion
    print(x)

imp(suma2(5,6))
    
    
#yield
#la palabra reservada -> yield <- se utiliza dentro de las funciones
#y sirve parecido a un return solo que en lugar de terminar la funcion
#solo la pausa para regresar el valor utilizarlo y despues regresa a la funcion

#ayuda a ahorrar memoria / optimiza recursos 

def returnlist():
    for num in range(0,10000000):
        yield num       #solo va a sacar un numero y no reverva toda la memoria

rango = range(0,1000000000)   #se reserva toda esa memoria 




