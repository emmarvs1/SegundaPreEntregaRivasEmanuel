#Saludo
print("Hola! Bienvenido a whatzqq, por favor, ingrese sus datos!")

#Input cliente
input("Ingrese su nombre aquí:")
def Usuario(nombre):
    nombre = "Emanuel";
print(Usuario)

#clase cliente
class Cliente:
    pass

    def __init__(self, nombre, apellido, direccion, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Direccion: {self.direccion}")
        print(f"Telefono: {self.telefono}")

#registro

Cliente1 = Cliente ("Emanuel","Rivas","watermelon 1564","1155648484")

Cliente1.mostrar_informacion()