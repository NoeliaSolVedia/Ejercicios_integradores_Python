'''
1. Escribir una función que calcule el máximo común divisor entre dos números.
2. Escribir una función que calcule el mínimo común múltiplo entre dos números
'''
'''
import math

def maximo_comun_divisor(a, b): 
    # Uso del algoritmo de Euclides
    mcd = 0
    A = max(a,b)
    B = min(a,b)
    while B != 0:
        mcd = B
        B = A % B
        A = mcd
    return mcd

def minimo_comun_multiplo(a, b):
    return (a*b)//maximo_comun_divisor(a, b)

def mcd(n, m):
    return math.gcd(n, m)
      
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
print("El MCD de",a,"y",b,"es:",maximo_comun_divisor(a,b))
print(f"El MCM de {a} y {b} es: {minimo_comun_multiplo(a, b)}")
'''

'''
3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
4. Escribir otra función que reciba el diccionario generado con la función anterior y 
devuelva una tupla con la palabra más repetida y su frecuencia.
'''
'''
def frecuencia(cad):
   palabras = cad.split()
   diccionario = {}
   for n in palabras:
     diccionario[n] = cad.count(n)
   return diccionario

def mas_repetida(dic):
  for key, value in dic.items():
     if value == max(dic.values()):
        tupla = (key,value)
  return tupla

#cadena = input("Ingrese una cadena de caracteres: ")
#cadena = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
cadena = "uno dos cuatro tres cuatro dos tres uno seis cinco dos"
print("Diccionario:",frecuencia(cadena))
print("Tupla:",mas_repetida(frecuencia(cadena)))
'''

'''
5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
ejercicio tanto de manera iterativa como recursiva.
'''
'''
def get_int_iterativo():
  ingreso_correcto  = False
  while not (ingreso_correcto):
    numero = input("Ingrese un número entero: ")
    try:
      numero = int(numero)
    except:
      print("ValueError: El valor ingresado no es válido para su conversión a entero. Intente nuevamente.")
    else:
      ingreso_correcto = True
  return numero

def get_int_recursivo():
    user_input = input('Por favor ingrese un número: ')
    try:
        value = int(user_input)
    except ValueError:
        print('No es un entero válido. Intente nuevamente!')
        return get_int_recursivo()
    else:
        return value

#print(f"Número ingresado: {get_int_iterativo()}")
print(f"Número ingresado: {get_int_recursivo()}")
'''
'''
6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
siguientes métodos para la clase:
• Un constructor, donde los datos pueden estar vacíos.
• Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
datos.
• mostrar(): Muestra los datos de la persona.
• es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
'''
class ErrorNombre(Exception):
    #Excepción lanzada se ingreso un nombre no válido
    def __init__(self, message='Nombre de persona no válido') :
        super().__init__(message)

class ErrorDni(Exception):
    #Excepción lanzada se ingreso un dni no válido
    def __init__(self, message='DNI de persona no válido') :
        super().__init__(message)
        
class ErrorEdad(Exception):
    #Excepción lanzada se ingreso una edad no válida
    def __init__(self, message='Edad de persona no válida') :
        super().__init__(message)

class Persona:
    def __init__(self,nombre="",edad=0,dni=0):
        self.__nombre = nombre 
        self.__edad = edad
        self.__dni = dni

    # setter y getter: atributo nombre
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        try:
            if (any(str.isdigit() for str in nuevo_nombre)): # any devuelve true si alguno de los  
                raise ErrorNombre()     #elementos del iterable es True
            self.__nombre = nuevo_nombre
        except ErrorNombre as en:
            print(f'Error:{en}')      

    # setter y getter: atributo edad
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, nueva_edad):
        try:
            nueva_edad = int(nueva_edad)
            if (nueva_edad < 0): # si no es una numero negativo
                raise ErrorEdad()        
            self.__edad = nueva_edad
        except ValueError:       #si no es un valor entero
            print("Error: Edad incorrecta") 
        except ErrorEdad as ee:
            print(f'Error:{ee}')    


    # setter y getter: atributo dni
    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self, nuevo_dni):
        try:
            nuevo_dni = int(nuevo_dni)
            if (nuevo_dni < 0 or nuevo_dni > 8): # si no es una numero negativo
                raise ErrorEdad()        
            self.__dni= nuevo_dni
        except ValueError:      #si no es un valor entero
            print("Error: Edad incorrecta") 
        except ErrorDni as ed:
            print(f'Error:{ed}')      

    # Métodos de la clase Persona
        
    def mostrar(self):
        return f'Persona:{self.nombre}, edad:{self.edad} años, DNI:{self.dni}'

    def es_mayor_de_edad(self):
        if (self.edad>=18):
            return "True"
        else:
            return "False"

#persona1 = Persona() # Creamos un objeto o instancia de la clase Persona
#persona1.mostrar()
#juan = Persona("Alejandro", 39, "29950013")
#juan.mostrar()
#juan.edad = -5
#juan.mostrar()

'''
7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Crear los siguientes métodos para la clase:
• Un constructor, donde los datos pueden estar vacíos.
• Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
directamente, sólo ingresando o retirando dinero.
• mostrar(): Muestra los datos de la cuenta.
• ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
• retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos.
'''
class ErrorNombreTitular(Exception):
    #Excepción lanzada se ingreso un nombre no válido para el titular de la cuenta
    def __init__(self, message='Nombre de persona no válido') :
        super().__init__(message)

class Cuenta: #Superclase
    def __init__(self,titular="",cantidad=0):
        self.titular = titular 
        self.__cantidad = cantidad

    # setter y getter: atributo titular
    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular     

    # getter: atributo cantidad

    @property
    def cantidad(self):
        return self.__cantidad

    # Metodos de la clase Cuenta

    def ingresar(self,cantidad):
        if (cantidad > 0):
           self.__cantidad = self.__cantidad + cantidad
           print(f'Deposito (${cantidad}) realizado con éxito')

    def retirar(self,cantidad):
        self.__cantidad = self.__cantidad - cantidad
        print(f'Extracción (${cantidad}) realizada con éxito')

    def mostrar(self):
        print(f'Titular de la Cuenta -->{self.titular.mostrar()} Cantidad:${self.cantidad}')

#titular = Persona("Alejandro", 39, "29950013")
#print(titular.mostrar())
#cuenta1 = Cuenta(titular,500) 
#cuenta1.ingresar(100) 
#cuenta1.mostrar()
#cuenta1.retirar(50) 
#cuenta1.mostrar()

'''
8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuentaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará expresada en
tanto por ciento. Crear los siguientes métodos para la clase:
• Un constructor.
• Los setters y getters para el nuevo atributo.
• En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
mayor de edad pero menor de 25 años y falso en caso contrario.
• Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
• El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
cuenta.
'''

class ErrorBonificacion(Exception):
    #Excepción lanzada se ingreso una edad no válida
    def __init__(self, message='Bonificacion no válida') :
        super().__init__(message)

class ErrorTitularNoValido(Exception):
    #Excepción lanzada se ingreso una edad no válida
    def __init__(self, message='El titular no posee una edad válida para poseer una Cuenta Jover') :
        super().__init__(message)

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion=0):
        super.__init__(titular, cantidad) # Atributos heredados
        self.__bonificacion = bonificacion # Atributo propio
        #self.agregarBonif()

    # setter y getter: atributo bonificacion
    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, bonificacion):
        try:
            if self.es_titular_valido(): # si no es una variable numerica real
                raise ErrorTitularNoValido()    
            if (bonificacion < 0): # si no es una numero negativo
                raise ErrorBonificacion()       
            self.__bonificacion = float(bonificacion)
            #self.agregarBonif(bonificacion)
        except ValueError:      #si no es un valor entero
            print("Error: Bonificación incorrecta") 
        except ErrorBonificacion as eb:
            print(f'Error:{eb}') 
        except ErrorTitularNoValido as etnv:
            print(f'Error:{etnv}')        

    # Metodos de la clase CuentaJoven
    def agregarBonif(self):
        if (self.bonificacion >= 0):
           self.cantidad = self.cantidad + self.cantidad*self.bonificacion*0.01

    def es_titular_valido(self):
        return (self.edad >=18 and self.edad <25)

    def retirar(self,cantidad):
        if self.es_titular_valido():
          self.cantidad = self.cantidad - cantidad
          print(f'Extracción (${cantidad}) realizada con éxito')
        else:
          print("La extracción no pudo realizarse: Titular no válido")

    def mostrar(self):
        print("------------ Cuenta Joven ------------")
        print(f"Titular --> {self.titular.mostrar()}, Cantidad: {self.cantidad}, Bonificación: {self.bonificacion}%")


persona = Persona("Mario",17,40623895)
print(persona.mostrar())
cuentaJoven1 = CuentaJoven(persona,500,20) 
cuentaJoven1.mostrar()
#cuentaJoven1.retirar(600) 
#cuentaJoven1.mostrar()
