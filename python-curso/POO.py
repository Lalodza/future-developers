#Programacion Orientada a Objetos
#clases de atributos y funciones
#-> class <- es la palabra reservada para iniciar una clase
#-> __init__ <-  es el constructor 
 
# pass      se utiliza para poder continuar con el codigo aunque
#           no terminemos al completo la funcion 
 
#en la terminal utilizamos
# $ from <nombre del script> import <nombre del objeto>
#ejemplo:
# $ from POO import Job

#y los valores del objeto los vamos a llenar asi:
# $ lalo = Job('Eduardo Diaz', 23, 1.70, 'developer'....)
# $ lalo.caminaAdelante(7)


class Person:
    
    nombre = ''
    edad = 0           #atributos o propiedades
    estatura = 0 
    posicion = 0
    
    def __init__(self, nombre, edad, estatura):     #se le pasan los parametros 
    
        self.nombre = nombre        
        self.edad = edad            #self  es como el this de otros lenguajes de programacion
        self.estatura = estatura
    
    def caminaAdelante(self, pasos):
        self.posicion += pasos
        print(f'{self.nombre} esta en: {self.posicion}')
        
    def caminaAtras(self, pasos):
        self.posicion -= pasos
        print(f'{self.nombre} regreso {self.posicion} pasos')
        
        
class Job(Person):    #al agregar un atibuto se genera una herencia de funciones
    
    trabajo = ''
    inicio = ''
    
    def __init__(self, nombre, edad, estatura, trabajo, inicio):
        self.nombre = nombre
        self.edad = edad
        self.estatura
        self.trabajo = trabajo
        self.inicio = inicio
        
 
        