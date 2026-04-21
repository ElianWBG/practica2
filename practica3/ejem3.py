# 1. El MIXIN: Su única función es registrar acciones
class AuditoriaMixin:
    def registrar_accion(self, mensaje):
        print(f"[AUDITORÍA]: {mensaje}")

# 2. La Clase Principal que usa el Mixin
class Producto(AuditoriaMixin):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self._precio = precio # El guion bajo _ indica que es "privado" (por convención)

    # 3. DECORADOR @property: Para LEER el precio
    @property
    def precio(self):
        return self._precio

    # 4. DECORADOR .setter: Para VALIDAR antes de escribir el precio
    @precio.setter
    def precio(self, nuevo_valor):
        if nuevo_valor <= 0:
            self.registrar_accion(f"Intento fallido: Precio inválido ({nuevo_valor})")
            print("Error: El precio debe ser mayor a 0.")
        else:
            self._precio = nuevo_valor
            self.registrar_accion(f"Cambio de precio a ${nuevo_valor} para {self.nombre}")

def ejecutar_sistema():
    inventario = [] # Nuestro arreglo (lista)
    
    # Creamos un producto
    p1 = Producto("Laptop", 1000)
    inventario.append(p1)
    
    print(f"Producto: {p1.nombre} | Precio actual: ${p1.precio}")

    # Intentamos cambiar el precio a algo malo
    print("\n--- Intentando poner precio negativo ---")
    p1.precio = -50 

    # Intentamos cambiar el precio a algo bueno
    print("\n--- Intentando poner precio correcto ---")
    p1.precio = 1200

    print(f"\nPrecio final de {p1.nombre}: ${p1.precio}")

if __name__ == "__main__":
    ejecutar_sistema()