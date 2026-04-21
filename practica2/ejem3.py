class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print(f"Producto: {self.nombre} | Precio: ${self.precio} | Stock: {self.stock}")

    def esta_disponible(self):
        return self.stock > 0


# funciones independientes (fuera de la clase)

def mostrar_todos(productos):
    for p in productos:
        p.mostrar_info()

def buscar_producto(productos, nombre):
    for p in productos:
        if p.nombre.lower() == nombre.lower():
            return p
    return None

def productos_disponibles(productos):
    disponibles = []
    for p in productos:
        if p.esta_disponible():
            disponibles.append(p)
    return disponibles


# programa principal

p  = Producto("manzana", 49, 10)
pa = Producto("pera", 423, 14)
pe = Producto("sandia", 0.20, 0)
pi = Producto("kiwi", 3, 100)

frutas = [p, pa, pe, pi]

print("=== Todos los productos ===")
mostrar_todos(frutas)

print("\n=== Buscar 'kiwi' ===")
encontrado = buscar_producto(frutas, "kiwi")
if encontrado:
    encontrado.mostrar_info()
else:
    print("No encontrado")

print("\n=== Solo disponibles ===")
for prod in productos_disponibles(frutas):
    prod.mostrar_info()