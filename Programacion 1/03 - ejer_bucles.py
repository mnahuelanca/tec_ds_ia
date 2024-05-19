"""1. Suma de Números Pares
Escribe un programa que calcule la suma de los primeros n números 
pares utilizando un bucle for."""
   
for i in range (1,21):
    if i % 2 == 0:
        suma = i+i
        print (f"{i} + {i} = {suma}")
        
"""2. Contador Regresivo
Escribe un programa que muestre un contador regresivo desde un 
número dado hasta 0 utilizando un bucle while"""

num =int(input("Dime un numero: "))

while num >= 0:
    print(num)
    num = num - 1

    
"""3. Tabla de Multiplicar
Escribe un programa que pida al usuario un número y muestre la tabla 
de multiplicar correspondiente utilizando un bucle for."""

numMulti = int(input("Dime un numero: "))

tabla = [0,1,2,3,4,5,6,7,8,9,10]

for i in tabla:
    resul = numMulti * i
    print(f"{numMulti} x {i} = {resul}")
    
"""4. Suma de Números hasta un Límite
Escribe un programa que solicite al usuario ingresar números enteros 
positivos y calcule la suma de todos los números ingresados hasta que 
el usuario ingrese un número negativo. Utiliza un bucle while para este 
propósito."""
numero = int(input("Ingrese un número: "))
suma = 0

while numero >= 0:
    suma += numero
    numero = int(input("Ingrese otro número: "))

print("La suma de los números ingresados es:", suma)

"""5. Patrón de Asteriscos
Escribe un programa que muestre un patrón de asteriscos como el 
siguiente utilizando un bucle for. Debe quedar así:
*
**
***
****"""

num = int(input("Ingrese un numero entero: "))

for i in range(1,num + 1):
    print(i * "*")