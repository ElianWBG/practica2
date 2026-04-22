from abc import ABC, abstractmethod

# 1. Definición de la Interfaz
class InterfazCRUD(ABC):
    @abstractmethod
    def registrar(self, objeto):
        pass

    @abstractmethod
    def consultar(self, id_objeto):
        pass

    @abstractmethod
    def eliminar(self, id_objeto):
        pass

# 2. Clases de Entidad (Modelos)
class Empleado:
    contador_id = 1
    def __init__(self, nombre, sueldo):
        self.id = Empleado.contador_id
        Empleado.contador_id += 1
        self.nombre = nombre
        self.sueldo = sueldo
        self.valor_hora = sueldo / 240

class TipoPermiso:
    contador_id = 1
    def __init__(self, descripcion, remunerado):
        self.id = TipoPermiso.contador_id
        TipoPermiso.contador_id += 1
        self.descripcion = descripcion
        self.remunerado = remunerado

class Permiso:
    contador_id = 1
    def __init__(self, id_empleado, id_tipo_permiso, fecha_desde, fecha_hasta, tipo, tiempo):
        self.id = Permiso.contador_id
        Permiso.contador_id += 1
        self.id_empleado = id_empleado
        self.id_tipo_permiso = id_tipo_permiso
        self.fecha_desde = fecha_desde
        self.fecha_hasta = fecha_hasta
        self.tipo = tipo
        self.tiempo = tiempo

# 3. Implementación del CRUD (Controlador)
class GestionPermisos(InterfazCRUD):
    def __init__(self):
        self.empleados = []
        self.tipos_permiso = []
        self.permisos = []

    def registrar(self, objeto):
        if isinstance(objeto, Empleado):
            self.empleados.append(objeto)
            print(f"Empleado '{objeto.nombre}' registrado con ID: {objeto.id}")
        elif isinstance(objeto, TipoPermiso):
            self.tipos_permiso.append(objeto)
            print(f"Tipo de Permiso '{objeto.descripcion}' registrado.")
        elif isinstance(objeto, Permiso):
            self.permisos.append(objeto)
            print(f"Permiso ID {objeto.id} registrado para el empleado {objeto.id_empleado}")

    def consultar(self, clase, id_objeto):
        lista = []
        if clase == Empleado: lista = self.empleados
        elif clase == TipoPermiso: lista = self.tipos_permiso
        elif clase == Permiso: lista = self.permisos
        
        for item in lista:
            if item.id == id_objeto:
                return item
        return None

    def eliminar(self, clase, id_objeto):
        objeto = self.consultar(clase, id_objeto)
        if objeto:
            if clase == Empleado: self.empleados.remove(objeto)
            elif clase == TipoPermiso: self.tipos_permiso.remove(objeto)
            elif clase == Permiso: self.permisos.remove(objeto)
            print(f"Registro con ID {id_objeto} eliminado.")
            return True
        print("Registro no encontrado.")
        return False

# --- Ejemplo de uso ---
gestion = GestionPermisos()

# Registrar un empleado
emp1 = Empleado("Juan Pérez", 2400)
gestion.registrar(emp1)

# Registrar un tipo de permiso
tipo1 = TipoPermiso("Cita Médica", True)
gestion.registrar(tipo1)

# Consultar datos
busqueda = gestion.consultar(Empleado, 1)
if busqueda:
    print(f"Consulta exitosa: {busqueda.nombre}, Valor hora: ${busqueda.valor_hora}")