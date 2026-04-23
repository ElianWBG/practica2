class empleado:
    _contador=0
    def __init__(self,letra1,promedio):
        empleado._contador+=1
        self.id=empleado._contador
        self.letra1=letra1
        self.promedio=promedio
        
    def promediar(self):
        return f" {self.id }-- {self.letra1}-- {self.promedio}"
class tipo_permiso:
    _contador=0
    def __init__(self,asd,dsa):
        tipo_permiso._contador+=1
        self.id=tipo_permiso._contador
        self.asd=asd
        self.dsa=dsa
    
    def presentarse(self):
        print(f"{self.id} -- {self.asd}-- {self.dsa} " )
pa=tipo_permiso("dsa","pepe")
pa.presentarse()
pe=tipo_permiso("elian",34)
pe.presentarse()
pi=tipo_permiso("jose",54)
pi.presentarse()

p=empleado("ABC",30)
p.promediar()
print(p.promediar())
agregar_cosas("Elian", 890)

#revisar
carritos=[]

def agregar_cosas(asd,dsa):
    e=tipo_permiso(asd,dsa)
    carritos.append(e)
    print(f" asd--{asd}---{dsa} metida exitosa ")
    
p.agregar_cosas("comidita")

def buscar_cosas(id):
    for e in carritos:
        if e.id==id:
            print("si esta aqui ")
            return
    return

def eliminar_cosas(id):
    for e in carritos:
        if e.id==id:
            carritos.remove(e)
    return

def menu():
    while True:
        print("primera opc")
        print("segunda opc")
        print("tercera opc ")
        print("salir pa ")
    
opc=input("Ingrese una opc 1-4 " )

if opc ==1:
    name=input("Ingrese name ")
    
if __name__=="__main__":
    menu()
    
# class Empleado:
#     _contador = 0

#     def __init__(self, nombre, promedio):
#         Empleado._contador += 1
#         self.id = Empleado._contador
#         self.nombre = nombre
#         self.promedio = promedio

#     def mostrar(self):
#         return f"{self.id} -- {self.nombre} -- {self.promedio}"


# class TipoPermiso:
#     _contador = 0

#     def __init__(self, nombre, valor):
#         TipoPermiso._contador += 1
#         self.id = TipoPermiso._contador
#         self.nombre = nombre
#         self.valor = valor

#     def presentarse(self):
#         print(f"{self.id} -- {self.nombre} -- {self.valor}")


# # Lista que actúa como base de datos temporal
# carritos = []


# def agregar_cosas(nombre, valor):
#     """Crea un TipoPermiso y lo agrega a la lista."""
#     e = TipoPermiso(nombre, valor)
#     carritos.append(e)
#     print(f"✔ '{nombre}' con valor '{valor}' agregado exitosamente.")


# def buscar_cosas(id):
#     """Busca un elemento por ID e imprime si existe."""
#     for e in carritos:
#         if e.id == id:
#             print(f"✔ Encontrado: {e.id} -- {e.nombre} -- {e.valor}")
#             return
#     print(f"✘ No se encontró ningún elemento con ID {id}.")


# def eliminar_cosas(id):
#     """Elimina un elemento de la lista por ID."""
#     for e in carritos:
#         if e.id == id:
#             carritos.remove(e)
#             print(f"✔ Elemento con ID {id} eliminado.")
#             return
#     print(f"✘ No se encontró ningún elemento con ID {id}.")


# def mostrar_todos():
#     """Muestra todos los elementos en la lista."""
#     if not carritos:
#         print("La lista está vacía.")
#     else:
#         print("\n--- Lista actual ---")
#         for e in carritos:
#             print(f"  {e.id} -- {e.nombre} -- {e.valor}")
#         print("--------------------\n")


# def menu():
#     while True:
#         print("\n========= MENÚ =========")
#         print("1. Agregar permiso")
#         print("2. Buscar permiso")
#         print("3. Eliminar permiso")
#         print("4. Mostrar todos")
#         print("5. Salir")
#         print("========================")

#         opc = input("Ingrese una opción (1-5): ").strip()

#         if opc == "1":
#             nombre = input("Ingrese nombre: ").strip()
#             valor = input("Ingrese valor: ").strip()
#             agregar_cosas(nombre, valor)

#         elif opc == "2":
#             try:
#                 id_buscar = int(input("Ingrese el ID a buscar: "))
#                 buscar_cosas(id_buscar)
#             except ValueError:
#                 print("✘ El ID debe ser un número entero.")

#         elif opc == "3":
#             try:
#                 id_eliminar = int(input("Ingrese el ID a eliminar: "))
#                 eliminar_cosas(id_eliminar)
#             except ValueError:
#                 print("✘ El ID debe ser un número entero.")

#         elif opc == "4":
#             mostrar_todos()

#         elif opc == "5":
#             print("Saliendo... ¡Hasta luego!")
#             break

#         else:
#             print("✘ Opción inválida. Ingrese un número entre 1 y 5.")


# if __name__ == "__main__":
#     menu()     