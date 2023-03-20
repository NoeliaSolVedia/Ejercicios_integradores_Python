'''
1. Escribir una función que calcule el máximo común divisor entre dos números.
2. Escribir una función que calcule el mínimo común múltiplo entre dos números
'''
'''
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
   for n in range(len(palabras)):
     diccionario[palabras[n]] = cad.count(palabras[n])
   return diccionario

def mas_repetida(dic):
  for key, value in dic.items():
     if value == max(dic.values()):
        tupla = (key,value)
  return tupla

cadena = input("Ingrese una cadena de caracteres: ")
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
def get_int():
  entero = False
  n = input("Ingrese un número entero: ")
  while (not entero):
   try:
     n = int(n)
     entero = True
   except:
     print("ValueError: El valor ingresado no es válido para su conversión a entero")
     n = input("Ingrese un entero nuevamente: ")
  return n

print("Número entero ingresado:",get_int())
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
    def __init__(self,nombre="",edad=None,dni=None):
        self.nombre = nombre 
        self.edad = edad
        self.dni = dni

    # setter y getter: atributo nombre

    def set_nombre(self,nombre):
        try:
            if (any(str.isdigit() for str in nombre)): # any devuelve true si alguno de los elementos del  
                raise ErrorNombre()                    # iterable que se da como argumento es True
            self.nombre = nombre
        except ErrorNombre as en:
            print(f'Error:{en}')      

    def get_nombre(self):
        print(f'Nombre: {self.nombre}')

    # setter y getter: atributo edad
    
    def set_edad(self, edad):
        try:
            if (not int(edad) == edad): # si no es una variable entera
                raise ErrorEdad()                  
            self.edad = edad
        except ErrorEdad as ee:
            print(f'Error:{ee}')      
        
    def get_edad(self):
        print(f'Edad: {self.edad}')

    # setter y getter: atributo dni
    
    def set_dni(self, dni):
        try:
            if (not int(dni) == dni): # si no es una variable entera
                raise ErrorDni()
            self.dni = dni
        except ErrorDni as ed:
            print(f'Error:{ed}')      
        
    def get_dni(self):
        print(f'DNI: {self.dni}')
    
    # Métodos de la clase Persona
        
    def mostrar(self):
        print(f'Persona: {self.nombre} con {self.edad} años y DNI: {self.dni}')

    def es_mayor_de_edad(self):
        if (self.edad>=18):
            return "True"
        else:
            return "False"

persona1 = Persona() # Creamos un objeto o instancia de la clase Persona
persona1.set_nombre("maria elena g4mez") 
persona1.get_nombre() 
#persona1.set_edad(58.5) 
#persona1.get_edad()
#persona1.set_edad(45) 
#persona1.get_edad()
#persona1.set_dni(35666777) 
#persona1.get_dni()
#persona1.es_mayor_de_edad()
'''

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
        self.titular=titular 
        self.cantidad=cantidad

    # setter y getter: atributo titular

    def set_titular(self,titular):
        try:
            if (any(str.isdigit() for str in titular)): # Si el nombre tiene un caracter no valido
                raise ErrorNombreTitular()                    
            self.titular = titular
        except ErrorNombreTitular as ent:
            print(f'Error:{ent}')      

    def get_titular(self):
        print(f'Titular: {self.titular}')

    # getter: atributo cantidad

    def get_cantidad(self):
        print(f'Cantidad: {self.cantidad}')

    # Metodos de la clase Cuenta

    def ingresar(self,cantidad):
        if (cantidad >= 0):
           self.cantidad = self.cantidad + cantidad
           print(f'Deposito (${self.cantidad}) realizado con éxito')

    def retirar(self,cantidad):
        self.cantidad = self.cantidad - cantidad
        print(f'Extracción (${cantidad}) realizada con éxito')

    def mostrar(self):
        print(f'Titular: {self.titular}\t\tCantidad: $ {self.cantidad}')

print("----------- Clase: Cuenta -----------")
cuenta1 = Cuenta("José") 
cuenta1.set_titular("José Rodrigue6z") 
#cuenta1.get_titular() 
#cuenta1.get_cantidad()
cuenta1.ingresar(480) 
cuenta1.mostrar()
cuenta1.retirar(600) 
cuenta1.mostrar()


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

class ErrorEdadCJ(Exception):
    #Excepción lanzada se ingreso una edad no válida
    def __init__(self, message='Edad de persona no válida') :
        super().__init__(message)

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion, edad):
        Cuenta.__init__(self, titular, cantidad) # Atributos heredados
        self.bonificacion = bonificacion # Atributo propio
        self.edad = edad
        self.agregarBonif(bonificacion)


    # setter y getter: atributo bonificacion

    def set_bonificacion(self,bonificacion):
        try:
            if (not float(bonificacion) == bonificacion): # si no es una variable numerica
                raise ErrorBonificacion()                  
            self.bonificacion = bonificacion
            self.agregarBonif(bonificacion)
        except ErrorBonificacion as eb:
            print(f'Error:{eb}')      

    def get_bonificacion(self):
        print(f'Bonificacion: %{self.bonificacion}')

    # setter y getter: atributo edad

    def set_edad(self, edad):
        try:
            if (not int(edad) == edad): # si no es una variable entera
                raise ErrorEdadCJ()                  
            self.edad = edad
        except ErrorEdadCJ as ee:
            print(f'Error:{ee}')      
        
    def get_edad(self):
        print(f'Edad: {self.edad}')


    # Metodos de la clase CuentaJoven
    def agregarBonif(self,bonificacion):
        if (bonificacion >= 0):
           self.cantidad = self.cantidad + self.cantidad*bonificacion*0.01

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
        print(f'Titular: {self.titular}\t\tCantidad: ${self.cantidad}\t\tBonificación: %{self.bonificacion}')


cuentaJoven1 = CuentaJoven("Mario",500,50,18) 
cuentaJoven1.mostrar()
cuentaJoven1.retirar(600) 
cuentaJoven1.mostrar()
