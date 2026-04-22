class empleado:
    _contador=0
    def __init__(self,nombre,sueldo):
        empleado._contador+=1
        self.id=empleado._contador
        self.nombre=nombre
        self.sueldo=sueldo
        self.valor_hora=sueldo/240
        
    
    def mostrar_info(self):
        print(f" el trabajador {self.id} -- {self.nombre} tiene un sueldo de {self.sueldo} y su hora {self.valor_hora}" )
        return
class tipo_permiso:
    _contador=0
    def __init__(self,descripcion,remunerado):
        tipo_permiso._contador+=1
        self.id=tipo_permiso._contador
        self.descripcion=descripcion
        self.remunerado=remunerado
    def mostrar_info(self):
        print(f" el trabajador{self.id}-- {self.descripcion} remunerado {self.remunerado} " )
class permiso:
    _contador=0
    def __init__(self,id_empleado,id_tipo_permiso,fecha_desde,fecha_hasta,tipo,tiempo):
        permiso._contador+=1
        self.id=permiso._contador
        self.id_empleado=id_empleado
        self.id_tipo_permiso=id_tipo_permiso
        self.fecha_desde=fecha_desde
        self.fecha_hasta=fecha_hasta
        self.tipo=tipo
        self.tiempo=tiempo
        
    
    def mostrar_info(self):
        print(f" {self.id}--{self.id_empleado}-- {self.id_tipo_permiso} -{self.fecha_desde}--{self.fecha_hasta}--{self.tipo}--{self.tiempo} " )
        return



empleados = []
tipos_permiso = []
permisos = []


def agregar_empleado(nombre,sueldo):
    e=empleado(nombre,sueldo)
    empleados.append(e)
    print(f" Empleado |{nombre} registrado con ID {e.id}")

def buscar_empleado(id):
    for e in empleados:
        if e.id==id:
            return e
    return

def eliminar_empleado(id):
    for e in empleados:
        if e.id==id:
            empleados.remove(e)
            print(f" Empleado {id} Eliminado ")
            return
    print(" Empleado no encontrado " )
def agregar_tipo_permiso(descripcion,remunerado):
    e=tipo_permiso(descripcion,remunerado)
    tipos_permiso.append(e)
    print(f"  los {id} {descripcion}--{remunerado}--")
def buscar_tipo_permiso(id):
    for e in tipos_permiso:
        if e.id==id:
            return e
    return
def eliminar_tipo_permiso(id):
    for e in tipos_permiso:
        if e.id==id:
            tipos_permiso.remove(e)
            print(f"Los permisos de {id} fueron eliminado")
            return
    print("Error eliminar los tipo de permisos " )

def agregar_permiso(id_empleado,id_tipo_permiso,fecha_desde,fecha_hasta,tipo,tiempo):
    e=permiso(id_empleado,id_tipo_permiso,fecha_desde,fecha_hasta,tipo,tiempo)
    permisos.append(e)
    print(f"{id_empleado}--{id_tipo_permiso}--{fecha_desde}--{fecha_hasta}--{tipo}--{tiempo}")
def buscar_permiso(id):
    for e in permisos:
        if e.id==id:
            return e
    return
def eliminar_permiso(id):
    for e in permisos:
        if e.id==id:
            permisos.remove(e)
            return
    print("Error al eliminar permiso ")

             



p=empleado("elian",560)
p.mostrar_info()
t1 = tipo_permiso("Enfermedad", "S")
t2 = tipo_permiso("Personal", "N")
t1.mostrar_info()
t2.mostrar_info()
per1 = permiso(1, 1, "2024-01-15", "2024-01-17", "D", 2)
per1.mostrar_info()
agregar_empleado("Elian", 890)
agregar_empleado("Maria", 1200)
buscar_empleado(1).mostrar_info()
eliminar_empleado(2)
        
def menu():
    while True:
        print("\n========================================")
        print("         SISTEMA DE PERMISOS")
        print("========================================")
        print("1. Registrar empleado")
        print("2. Registrar tipo de permiso")
        print("3. Registrar permiso")
        print("4. Consultar registros")
        print("5. Eliminar registro")
        print("6. Salir")
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            registro_empleado()
        elif opcion == "2":
            registro_tipo_permiso()
        elif opcion == "3":
            registro_permiso()
        elif opcion == "4":
            consultar()
        elif opcion == "5":
            eliminar()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion invalida")

menu()
def registro_empleado():
    print("\n--- REGISTRO DE EMPLEADO ---")
    nombre = input("Nombre: ")
    sueldo = float(input("Sueldo: "))
    # tú completas...