"""Ejercicio N°1
Crear una función que eleve un número al cuadrado y lo imprima."""

def nCuadrado():
    n = int(input("Ingrese un numero: "))
    
    cuad = n*n
    
    print (cuad)

nCuadrado()
"""Ejercicio N°2
Crear una función que calcule el IVA de un producto y lo imprima con 
la leyenda “El IVA correspondiente al (valor ingresado) es (resultado 
de la función)."""
def iva():
    precioProducto = float(input("Cual es el precio del producto?: $"))
    valorIva = 0.21
    
    precioIva = precioProducto * valorIva
    
    valorTotal = precioProducto + precioIva
    
    print(f"El IVA correspondiente al ${precioProducto} es ${precioIva}. Esto es un valor total de ${valorTotal}")
    
iva()

"""Ejercicio N°3
Crear una función que realice la suma, resta, división y multiplicación 
de dos números y lo imprima con el nombre de cada operación. 
a) Si el usuario introduce 1, que sume dos números. 
b) Si el usuario introduce 2, reste dos números. 
c) Si el usuario introduce 3, multiplique dos números 
d) Si el usuario introduce 4, divida dos números"""

def cuentas():
    opciones = input("""
Ingrese una opcion:
    1 = sumar dos numeros
    2 = restar dos numeros
    3 = multiplicar dos numeros
    4 = dividir dos numeros
:""")
    
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    
    if opciones == "1":
        resul = num1 + num2
        print (resul)
    elif opciones == "2":
        resul = num1 - num2
        print (resul)
    elif opciones == "3":
        resul = num1 * num2
        print (resul)
    elif opciones == "4":
        resul = num1 / num2
        print (resul)
    else:
        print("Opcion invalida")

cuentas()

