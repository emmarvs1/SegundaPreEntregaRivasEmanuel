
from modulo1 import Cliente

print(Cliente)

print("Hola! Emanuel")

#Items de Hamburgueseria
print("Elige la hamburguesa que desea comprar! incluye papas fritas!:")

class Tienda:
   
    pass
   
    def __init__(self,articulo,descripcion,valor,categoria):
        self.Items=[]
        self.articulo = articulo
        self.descripcion = descripcion
        self.valor = valor
        self.categoria = categoria
    def __str__(self) -> str:
        return f"Articulo:{self.articulo} descripcion:{self.descripcion} Valor:{self.valor} Categoria:{self.categoria}"
        
Compra1 =   Tienda("Thor","Triple carnce, triple cheddar y triple panceta", "5000", "comida")
Compra2 =   Tienda("Loki","Triple carne, cebolla caramelizada, SSB y doble cheddar", "5750", "comida")
Compra3 =   Tienda("Odin", "Quintuple carne, triple cheddar, triple panceta, huevo frito y salsa armaggedon", "7500","comida")
Compra4 =   Tienda("Balder","Doble carne, lechuga, tomate", "5000","comida")

print("Elegiste comprar:")

print(Compra1,Compra2,Compra3,Compra4);

#Valor total Carrito

# Calcular el total del carrito

# Inicializar una lista para el carrito de compras
carrito_de_compras = []

# Función para agregar un producto al carrito
def agregar_producto(producto, precio):
    carrito_de_compras.append({"producto": producto, "precio": precio})
    print(f"{producto} agregado al carrito.")

# Función para mostrar el contenido del carrito
def mostrar_carrito():
    if not carrito_de_compras:
        print("El carrito de compras está vacío.")
    else:
        print("Contenido del carrito:")
        total = 0
        for item in carrito_de_compras:
            print(f"{item['producto']} - Precio: ${item['precio']}")
            total += item['precio']
        print(f"Total de la compra: ${total}")

# Loop principal
while True:
    print("\n1. Agregar producto al carrito")
    print("2. Mostrar carrito")
    print("3. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        producto = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        agregar_producto(producto, precio)
    elif opcion == "2":
        mostrar_carrito()
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")