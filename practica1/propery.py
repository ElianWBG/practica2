class Libro:
    def __init__(self, titulo, precio):
        self.titulo = titulo
        self._precio = precio  # El guion bajo indica que es "privado"

    @property
    def precio(self):
        """Este es el GETTER: Sirve para LEER el valor"""
        print("Consultando el precio...")
        return f"${self._precio}"

    @precio.setter
    def precio(self, nuevo_precio):
        """Este es el SETTER: Sirve para ESCRIBIR/CAMBIAR el valor"""
        if nuevo_precio < 0:
            print("❌ ERROR: El precio no puede ser negativo.")
        else:
            print(f"✅ Precio actualizado a {nuevo_precio}")
            self._precio = nuevo_precio

# --- Uso ---
mi_libro = Libro("Python Básico", 20)

# Lo usamos como una variable normal (sin paréntesis)
print(mi_libro.precio)  # Ejecuta el @property

mi_libro.precio = 25    # Ejecuta el @precio.setter
mi_libro.precio = -5    # ¡Aquí el setter nos protege del error!