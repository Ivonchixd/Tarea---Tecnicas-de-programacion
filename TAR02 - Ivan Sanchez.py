# Ivan Geronny Sanchez Mancebo 21-1980
# Escribir un programa que pida 2 números y muestre paso a paso el cálculo de la raíz cuadrada de la suma del cuadrado de ambos:
   #Importamos el modulo math para tener acceso a las funciones matematicas.
import math
''' Declaramos las variables y se utiliza la funcion input para que el usuario pueda introducir por teclado un numero.
    Por lo mismo tanto, se utiliza int para especificar el tipo de dato a introducir.'''
num1 = int(input('Introduzca el primer numero: '))
num2 = int(input('Introduzca el segundo numero: '))

''' Variables para optimizar las lineas de codigo y facilitar el entendimiento de la suma(Funcionamiento del programa en general).
    De igual forma, estas variables son para almacenar la suma de ambas potencias.'''
num_s1 = num1**2
num_s2 = num2**2

   #Variable para la suma total.
num_st = (num_s1 + num_s2)

   #Se detalla lo que el programa va a imprimir paso a paso:
   #Primero se organiza el calculo de la potencia de los numeros introducidos por el usuario
print("Operacion a realizar con los numeros introducidos:", '√(({})^2 + ({})^2) = '.format(num1, num2))
   #Luego se realiza la suma, ya con sus potencias
print("La suma de potencias es:", '√({} + {}) = '.format(num1**2, num2**2))
   #Resultado de la suma, con su formato para raiz cuadrada
print('√', num_s1 + num_s2)
   #Llamamos el modulo math pero para la funcion de raiz cuadrada (sqrt) y se consigue la raiz cuadrada de esa suma total de potencias.
print('La raiz cuadrada es: ', math.sqrt(num_st))