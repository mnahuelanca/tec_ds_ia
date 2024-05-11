"""Ejercicio N°1
Verificación de edad para ver una película
Supongamos que estás desarrollando un programa para un cine y 
deseas asegurarte de que los espectadores sean lo suficientemente 
mayores para ver una película clasificada como PG-13. 
Debes solicitar la edad del espectador y permitir el acceso solo si 
tienen al menos 13 años.
"""

edad = int(input("¿Cual es tu edad?: "))

if edad > 12:
    print ("Puedes pasar")
else:
    print("No puedes pasar")

"""Ejercicio N°2
Calificación de un estudiante
Imagina que eres un profesor y deseas calcular las calificaciones 
finales de tus estudiantes en función de sus puntajes en un examen. 
La calificación final se asignará de la siguiente manera: 
Si el puntaje…
Es mayor o igual a 90, la calificación es "A".
Está entre 80 y 89, la calificación es "B".
Está entre 70 y 79, la calificación es "C".
Está entre 60 y 69, la calificación es "D".
Es menor que 60, la calificación es "F"""

nota = int(input("¿Cual fue la nota?: "))

if nota >= 90:
    print("Calificacion A")
elif nota >= 80 and nota <=89:
    print("Calificacion B")
elif nota >= 70 and nota <=79:
    print("Calificacion C")
elif nota >= 60 and nota <=69:
    print("Calificacion D")
else:
    print ("Calificacion F")

"""Ejercicio N°3
Calculadora de descuento
Ahora debes generar un programa calcule el descuento de un 
producto, se le solicita al usuario ingresar el precio original de un 
producto. Luego, calcula y muestra el precio final después del 
descuento. 
Tener en cuenta lo siguiente: 
Si se ingresa un precio de producto mayor o igual a $12.999
entonces se realizará el descuento del 30%, 
Sino, se realizará el descuento del 20% sobre el total del 
producto"""

precio = float(input("¿Cual es el precio?: $"))

if precio >= 12.99:
    desc30 = (precio / 100) * 30
    print(f"El precio original de ${precio}, tiene un descuento del 30% equivalente a ${desc30}. El precio final es de ${precio-desc30}")
else:
    desc20 = precio / 100 * 2
    print(f"El precio original de ${precio}, tiene un descuento del 20% equivalente a ${desc20}. El precio final es de ${precio-desc20}")


"""Ejercicio N°4
Validar dias de la semana
Crea un programa que pida al usuario ingresar un número del 1 al 7 y 
muestre el día de la semana correspondiente. Si ingresa un número 
fuera de ese rango, mostrar el siguiente mensaje de error: "Número 
de día incorrecto"""

dia = int(input("Ingrese un numero del 1 al 7: "))

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miercoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sabado")
elif dia == 7:
    print("Domingo")
else:
    print("Numero de dia incorrecto")



"""Ejercicio N°5
El mayor de tres números
Crea un programa que solicite al usuario ingresar tres números y 
determine cuál es el mayor de los tres, luego informa al usuario con 
un mensaje cual es el número mayor"""

num1 = int(input("Ingrese un 1er numero: "))
num2 = int(input("Ingrese un 2do numero: "))
num3 = int(input("Ingrese un 3er numero: "))


if num1 > num2 and num1 > num3:
    print(f"El mayor numero de los tres ingresados es {num1}")
elif num2 > num1 and num2 > num3:
    print(f"El mayor numero de los tres ingresados es {num2}")
else:
    print(f"El mayor numero de los tres ingresados es {num3}")

"""Ejercicio N°6
Notas de un alumno
Crea un programa que determine y muestre al alumno, según la nota 
que ingrese, a que categoría pertenece de calificación. Si la nota no 
corresponde con las categorías, mostrar el mensaje "La nota 
ingresada es invalida". Las categorías son: 
Suspenso → Notas: 0, 1, 2, 3, 4 y 5 
Aprobado → Nota: 6 
Buena → Nota: 7 
Notable → Nota: 8 
Sobresaliente → Notas: 9 y 10"""

notaAlumno = int(input("Cual fue tu nota?: "))

if notaAlumno >= 0 and notaAlumno <=5:
    print("Suspenso")
elif notaAlumno == 6:
    print("Aprobado")
elif notaAlumno == 7:
    print("Buena nota")
elif notaAlumno == 8:
    print("Notable")
elif notaAlumno == 9 or notaAlumno == 10:
    print("Sobresaliente")
else:
    print("La nota ingresas es invalida")

"""Ejercicio N°7
Validar altura de una persona
Realizar un programa calcule si una persona es de estatura baja, 
media o alta. En tales casos, informar…
Si la altura es menor o igual a 150 cm → “Persona de altura 
baja”; 
Si la altura está entre 151 y 170 → “Persona de altura media”
Si la altura es mayor al 171 → “Persona alta”"""

altura = int(input("Ingrese su altura en cm: "))

if altura <= 150:
    print("Persona de altura baja")
elif altura >= 151 and altura <= 170:
    print("Persona de altura media")
elif altura > 170:
    print("Persona alta")


"""Ejercicio N°8
Calculas precio final del envío
Una empresa de transporte ofrece su servicio para enviar paquetes a 
tres provincias de la Patagonia Argentina. 
Cuando un cliente quiere enviar un paquete, puede elegir por 
distintos tipos de pesos Ej: (paquete de 15 kg a 20 kg). El cliente 
contrata el servicio de transporte eligiendo una provincia como 
destino y un peso de paquete. 
Se necesita realizar un algoritmo para saber el precio final a pagar. 
En la siguiente tabla se muestran los destinos con cada peso 
admitido y su precio correspondiente"""


provincia = int(input(
    """Hola, porfavor indique con un numero a que provincia desea su envio:
    1 = Santa Cruz,
    2 = Chubut,
    3 = Rio Negro
    """))

if provincia == 1:
    peso = int(input(
        """Hacia la provincia de Santa Cruz. Indiquenos el peso de su envio:
        1 = Menor a 5kg
        2 = Entre 6 kg y 10 kg
        3 = Entre 11 kg y 20kg
        """))
    if peso == 1:
        print ("El precio por su envio es de $200")
    elif peso == 2:
        print ("El precio por su envio es de $300")
    elif peso == 3:
        print ("El precio por su envio es de $400")

elif provincia == 2:
    peso = int(input(
        """Hacia la provincia de Chubut. Indiquenos el peso de su envio:
        1 = Menor a 10kg
        2 = Entre 11 kg y 15 kg
        3 = Entre 16 kg y 25kg
        """))
    if peso == 1:
        print ("El precio por su envio es de $350")
    elif peso == 2:
        print ("El precio por su envio es de $390")
    elif peso == 3:
        print ("El precio por su envio es de $420")

elif provincia == 3:
    peso = int(input(
        """Hacia la provincia de Rio Negro. Indiquenos el peso de su envio:
        1 = Menor a 12kg
        2 = Entre 13 kg y 18 kg
        3 = Entre 19 kg y 26kg
        """))
    if peso == 1:
        print ("El precio por su envio es de $400")
    elif peso == 2:
        print ("El precio por su envio es de $480")
    elif peso == 3:
        print ("El precio por su envio es de $510")