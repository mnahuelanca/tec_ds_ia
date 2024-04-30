#Actividades

#1. Operadores relacionales: Crea un programa que compare dos números y determine si el primero es mayor que el segundo.
num1 = 1
num2 = 5

if(num1>num2):
    print(str(num1) + " es mayor que " + str(num2))
else:
    print(str(num1) + " es menor que " + str(num2))


#2. Operadores lógicos: Construye un programa que determine si un número ingresado por el usuario es par y positivo al mismo tiempo.
n_usu = int(input("Digite un numero: "))

if (n_usu % 2 == 0 and n_usu > 0):
    print("El numero ingresado es PAR y POSITIVO")
else:
    print("El numero ingresado NO es PAR")


#3. Conversión de tipos: Realiza una concatenación de una cadena y un número, convirtiendo el número a cadena.
cadena = "El precio es "
precio = 500

conca = cadena + str(precio)
print(conca)


#4. Expresiones condicionales: Crea un programa que determine si un año ingresado por el usuario es un año bisiesto o no, usando expresiones lógicas.
anio = int(input("ingresa un año: "))


#5. Expresiones complejas: Escribe un programa que determine si un número es divisible por 3 y 5 al mismo tiempo.
