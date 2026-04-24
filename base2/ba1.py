# def decorador_interfaz(titulo):          # (1) Función externa — recibe el título
#     def wrapper(func):                   # (2) Función media — recibe la función a decorar
#         def inner(*args, **kwargs):      # (3) Función interna — es lo que realmente se ejecuta
#             print("=" * 40)
#             print(f"{titulo.center(40)}")  # Imprime el título centrado
#             print("=" * 40)
#             res = func(*args, **kwargs)    # Llama a la función original
#             return res
#         return inner
#     return wrapper

# def con_separador(func):
#     def envoltura(*args):
#         print("----------")
#         func(*args)
#         print("----------")
#     return envoltura
# @con_separador
# def saludar(nombre):
#     print(f"Hola, {nombre}! ")

# @con_separador
# def despedir(nombre):
#     print(f"Adios, {nombre}!")

# saludar("Ana")
# despedir("Ana")


# def funciona(funcionb):
#     def funcionc(*args):
#         print("----------")
#         funcionb(*args)
#         print("----------")
#     return funcionc
# @funciona
# def saludar(nombre):
#     print(f"Hola,{nombre}")

# @funciona
# def despedir(nombre):
#     print(f"Adios,{nombre}")
    
# saludar("pedro")
# despedir("Jose")







def Antes_d(Despues_D):
    def mediod(*args):
        print("usuario ejecuto borrar roles " )
        Despues_D(*args)
        print("usuario Salio de roles ")
    return mediod

@Antes_d
def Saludar(nombre):
    print(f" {nombre}, Entrando a roles ")
@Antes_d
def Despedir(nombre):
    print(f" {nombre}, saliendo de ")

Saludar("elian")
Despedir("Jhoan")

print("-----------------")
print("-----------------")


class volarmix():
    def volar(self):
        print(f" {self.nombre} esta volando! ")
        
class pajaro(volarmix):
    def __init__(self,nombre):
        self.nombre=nombre
class murcielago(volarmix):
    def __init__(self,nombre):
        self.nombre=nombre
    
class perro():
    def __init__(self,nombre):
        self.nombre=nombre

p = pajaro("Piolín")
m = murcielago("Bruce")
d = perro("Rex")

p.volar()    # Piolín está volando!
m.volar()    # Bruce está volando!
d.volar()    # ERROR — Perro no hereda VolarMixin




