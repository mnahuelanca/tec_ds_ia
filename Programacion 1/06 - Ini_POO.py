#Defino una clase
class Persona:

    #Defino constructor de la clase persona con atributos.
    def __init__(self, nombre, apellido, edad, ciudad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ciudad = ciudad
    
    #Metodo que imprime un string
    def saludar(self):
        print(f"Hola! mi nombre es {self.nombre} {self.apellido}. Tengo {self.edad} años y vivo en {self.ciudad}")

persona1 = Persona("Juan","Perez",30,"Rio Grande")
persona1.saludar()