class Admin: # Las clases suelen empezar con Mayúscula
    def __init__(self, nombre, contraseña):
        self._nombre = nombre
        self._contraseña = contraseña # Usamos un solo _ por consistencia

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre) < 3:
            print("Nombre demasiado corto")
        else:
            self._nombre = nuevo_nombre

    @property
    def contraseña(self):
        return "********" # Por seguridad, a veces el getter oculta la clave real

    @contraseña.setter
    def contraseña(self, valor):
        # Medimos el largo de la nueva contraseña
        seguridad = len(valor) 

        # Evaluamos de mayor a menor para que la lógica funcione
        if seguridad >= 15:
            print("La contraseña es excelente y muy segura")
            self._contraseña = valor
        elif seguridad >= 10:
            print("Contraseña aceptable, pero podría ser mejor")
            self._contraseña = valor
        else:
            print("Error: Falta seguridad (mínimo 10 caracteres)")
a=Admin("elian",2131)
print(a.contraseña) 
print(a.nombre)    
    