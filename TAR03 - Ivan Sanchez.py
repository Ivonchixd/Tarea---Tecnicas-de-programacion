# Ivan Geronny Sanchez Mancebo 21-1980
""" Escriba un programa que calcule el precio a pagar por el suministro de energía eléctrica. 
Se debe preguntar la cantidad de kwh consumidos y el tipo de instalación: R para residencias, 
I para industrias y C para comercios. Calcule el precio a pagar de acuerdo con la tabla."""

#Declaramos la variable para que el usuario pueda introducir el tipo de instalacion deseado.
install_type = input('''
-Seleccione el tipo de instalacion electrica:
r para residencias...
i para industrias...
c para comercios...
''')

#Variables para los diferentes precios (De esta forma para que sea mas facil el mantenimiento del programa).
precio_r1 = 'RD$550.00'
precio_r2 = 'RD$850.00'
precio_i1 = 'RD$3800.00'
precio_i2 = 'RD$4200.00' 
precio_c1 = 'RD$1300.00'
precio_c2 = 'RD$2500.00'

#Declaramos la variable con input / int para que el usuario introduzca la cantidad de kwh que pide el programa.
num_kwh = int(input('Introduzca la cantidad de kwh consumidos: '))

#Condiciones if/elif/else para poder determinar la seleccion del usuario y lo que el programa va a mostrar.
#Se llama la variable anteriormente declarada para los tipos de instalamiento.
if install_type == 'r' and num_kwh <= 500:
    print("Sus kwh consumidos son de hasta:", num_kwh)
    print("Su precio es: ", precio_r1)
elif install_type == 'i' and num_kwh <= 5000:
    print("Sus kwh consumidos son de hasta:", num_kwh)
    print("Su precio es: ", precio_i1)
elif install_type == 'c' and num_kwh <= 1000:
    print("Sus kwh consumidos son de hasta:", num_kwh)
    print("Su precio es: ", precio_c1)
#Por motivos de facilitar el entendimiento del codigo general, esta de cierta forma mas detallada cada linea de codigo.
else:
    if install_type == 'r' and num_kwh >= 500:
        print("Sus kwh consumidos son mas de:", num_kwh)
        print("Su precio es: ", precio_r2)
    elif install_type == 'i' and num_kwh >= 5000:
        print("Sus kwh consumidos son mas de:", num_kwh)
        print("Su precio es: ", precio_i2)
    elif install_type == 'c' and num_kwh >= 1000:
        print("Sus kwh consumidos son mas de:", num_kwh)
        print("Su precio es: ", precio_c2)