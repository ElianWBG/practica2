# 1. El decorador lo usaremos para las NOTIFICACIONES
def validar_notificacion(funcion_original):
    def envoltorio(*args, **kwargs):
        print("🔍 Validando estado financiero...")
        resultado = funcion_original(*args, **kwargs)
        print("📢 Notificación enviada al gerente.")
        return resultado
    return envoltorio

# 2. Clases base (Sin el decorador en la clase, sino en sus métodos)
class EquipoFut:
    def __init__(self, nombre, plantilla, escudo, valor):
        self.nombre = nombre
        self.plantilla = plantilla
        self.escudo = escudo
        self.valor = valor

    def mostrar_equipo(self): # <--- FUERA del __init__
        print(f"Equipo: {self.nombre}, Valor: {self.valor}M")

class JugadorFut:
    def __init__(self, nombre, posicion, valor):
        self.nombre = nombre
        self.posicion = posicion
        self.valor = valor

    @validar_notificacion # <--- El decorador va en la acción
    def entrenar(self):
        print(f"🏃 {self.nombre} está entrenando duro.")

# 3. Sponsor como una clase independiente (o Mixin si fuera necesario)
class Sponsor:
    def __init__(self, nombre_sponsor, inversion):
        self.nombre_s = nombre_sponsor
        self.inversion = inversion

# --- PRUEBAS ---
print("--- Ejemplo de uso ---")
equipo1 = EquipoFut("Barcelona", 25, "Escudo", 1000)
jugador1 = JugadorFut("Lionel Messi", "Delantero", 150)

equipo1.mostrar_equipo()
jugador1.entrenar() # Aquí se activa el decorador