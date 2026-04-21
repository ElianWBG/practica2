# 1. Este es nuestro Mixin (La "herencia" de una habilidad)
class VolarMixin:
    def volar(self):
        print(f"¡Mira! {self.nombre} está surcando los cielos ☁️")

# 2. Clase base: Un personaje normal
class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre

# 3. El Guerrero NO vuela, solo hereda de Personaje
class Guerrero(Personaje):
    def atacar(self):
        print(f"{self.nombre} ataca con su espada ⚔️")

# 4. El Dragon SI vuela, así que le "añadimos" el Mixin
class Dragon(Personaje, VolarMixin): # <--- Aquí ocurre la magia
    def escupir_fuego(self):
        print(f"{self.nombre} lanza una bola de fuego 🔥")

# --- Pruebas ---
ragnar = Guerrero("Ragnar")
ragnar.atacar()
# ragnar.volar()  <-- Esto daría error, los guerreros no vuelan.

drogon = Dragon("Drogon")
drogon.escupir_fuego()
drogon.volar() # <-- ¡Heredó la habilidad del Mixin!
##OTRO EJEMPLO PADRE DE LOS MIX IN 
# Clase 1: Habilidad de Movimiento
class CaminarMixin:
    def caminar(self):
        print("Caminando sobre dos piernas... 👣")

# Clase 2: Habilidad de Combate
class DispararMixin:
    def disparar(self):
        print("¡Piu! ¡Piu! Disparando láseres... 🔫")

# Clase 3: Habilidad de Comunicación
class HablarMixin:
    def hablar(self, mensaje):
        print(f"El robot dice: '{mensaje}' 🤖")

# --- LA MEZCLA ---
class SuperRobot(CaminarMixin, DispararMixin, HablarMixin):
    def encender(self):
        print("Sistema iniciado.")

# Ahora el SuperRobot puede usar TODO
mi_robot = SuperRobot()
mi_robot.caminar()   # De la clase 1
mi_robot.disparar()  # De la clase 2
mi_robot.hablar("Hola, Elian") # De la clase 3