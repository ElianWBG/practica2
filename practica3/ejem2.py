class Producto:
    def __init__(self, nombre, precio):
        # Usamos self.nombre y self.precio para que pasen por los setters desde el inicio
        self.nombre = nombre
        self.precio = precio

    # --- Propiedad Nombre ---
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    # --- Propiedad Precio ---
    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        if valor > 0:
            self.__precio = valor
        else:
            # Mensaje exacto de tu imagen
            print("Precio inválido, debe ser mayor a 0")

    # --- Método Categoría ---
    def categoria(self):
        if self.__precio < 50:
            print("Económico")
        elif self.__precio < 200:
            print("Estándar")
        else:
            print("Premium")

# --- Prueba del código ---
p = Producto("Laptop", 800)
print(p.nombre)    # Salida: Laptop
print(p.precio)    # Salida: 800

p.precio = -10     # Salida: Precio inválido, debe ser mayor a 0
p.precio = 200    # Actualiza el precio a 45
print(p.precio)    # Salida: 45

p.categoria()      # Salida: Económico