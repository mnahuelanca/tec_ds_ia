#Un palíndromo es una palabra o frase que se lee igual en un sentido que en otro
#Somos o no somos 
#Solos

def palindromo():
    while True:
        palabra = input("Escribe una palabra: ")
        palabra_original = palabra.replace(" ", "").lower()  # Elimina los espacios y transforma a minúsculas
        palabra_invertida = palabra_original[::-1]  # Invierte la palabra
        if palabra_original == palabra_invertida:
            print("Es palindromo")
        else:
            print("No es palindromo")
        continuar = input('Quiere continuar con otra palabra? si=1 / no=2: ')
        if continuar == '2':
            print('Hasta luego!')
            break

palindromo()

