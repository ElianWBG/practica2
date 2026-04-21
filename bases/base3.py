import os
from abc import ABC, abstractmethod
from datetime import datetime

# =========================================================
# 1. DECORADORES (Para validación y utilidades)
# =========================================================
def validar_datos(func):
    """Decorador para asegurar que la entrada no sea vacía."""
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except ValueError as e:
                print(f"Error: {e}. Intente de nuevo.")
    return wrapper

# =========================================================
# 2. MIXINS (Funcionalidades compartidas)
# =========================================================
class FormatterMixin:
    """Proporciona formato de moneda y limpieza de pantalla."""
    def format_money(self, amount):
        return f"${amount:,.2f}"

    def clean_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

# =========================================================
# 3. INTERFACES CRUD (Clase Abstracta)
# =========================================================
class ICrud(ABC):
    @abstractmethod
    def create(self): pass
    
    @abstractmethod
    def read(self): pass
    
    @abstractmethod
    def delete(self): pass

# =========================================================
# 4. MODELOS DE DATOS
# =========================================================
class Empleado:
    next_id = 1
    def __init__(self, nombre, sueldo):
        self.id = Empleado.next_id
        Empleado.next_id += 1
        self.nombre = nombre
        self.sueldo = float(sueldo)
        self.valor_hora = self.sueldo / 240

class TipoPermiso:
    next_id = 1
    def __init__(self, descripcion, remunerado):
        self.id = TipoPermiso.next_id
        TipoPermiso.next_id += 1
        self.descripcion = descripcion
        self.remunerado = remunerado # Booleano (True/False)

class Permiso:
    next_id = 1
    def __init__(self, emp_id, tipo_id, desde, hasta, tipo_dh, tiempo, descuento=0):
        self.id = Permiso.next_id
        Permiso.next_id += 1
        self.emp_id = emp_id
        self.tipo_id = tipo_id
        self.desde = desde
        self.hasta = hasta
        self.tipo_dh = tipo_dh # D o H
        self.tiempo = tiempo
        self.descuento = descuento

# =========================================================
# 5. LÓGICA DEL SISTEMA (CORE)
# =========================================================
class SistemaPermisos(ICrud, FormatterMixin):
    def __init__(self):
        self.empleados = []
        self.tipos_permisos = []
        self.permisos = []

    # --- MÉTODOS DE REGISTRO (CREATE) ---
    @validar_datos
    def create_empleado(self):
        self.clean_screen()
        print("="*40 + "\n      REGISTRO DE EMPLEADO\n" + "="*40)
        nombre = input("Nombre: ")
        sueldo = float(input("Sueldo: "))
        valor_hora = sueldo / 240
        print("-" * 40)
        print(f"Valor hora calculado: {self.format_money(valor_hora)}")
        
        op = input("¿Desea guardar? (1. Sí / 2. No): ")
        if op == "1":
            self.empleados.append(Empleado(nombre, sueldo))
            print("Empleado guardado con éxito.")

    @validar_datos
    def create_tipo_permiso(self):
        print("="*40 + "\n      TIPO DE PERMISO\n" + "="*40)
        desc = input("Descripción: ")
        remu = input("¿Remunerado? (S/N): ").upper() == 'S'
        if input("¿Guardar? (1. Sí / 2. No): ") == "1":
            self.tipos_permisos.append(TipoPermiso(desc, remu))

    @validar_datos
    def create_permiso(self):
        print("="*40 + "\n      REGISTRO DE PERMISO\n" + "="*40)
        emp_id = int(input("ID Empleado: "))
        tipo_id = int(input("ID Tipo Permiso: "))
        
        # Búsqueda usando funciones de orden superior (filter / next)
        emp = next((e for e in self.empleados if e.id == emp_id), None)
        tp = next((t for t in self.tipos_permisos if t.id == tipo_id), None)

        if not emp or not tp:
            print("Error: Empleado o Tipo de Permiso no existe.")
            return

        f_desde = input("Fecha desde (DD/MM/AAAA): ")
        f_hasta = input("Fecha hasta (DD/MM/AAAA): ")
        t_dh = input("Tipo (D: Día / H: Hora): ").upper()
        tiempo = float(input("Cantidad de tiempo: "))

        # Cálculo de descuento si NO es remunerado
        descuento = 0
        if not tp.remunerado:
            factor = 8 if t_dh == 'D' else 1 # Si es día, son 8 horas
            descuento = tiempo * factor * emp.valor_hora

        print("-" * 40 + "\nResumen:")
        print(f"¿Remunerado?: {'Sí' if tp.remunerado else 'No'}")
        print(f"Descuento aplicado: {self.format_money(descuento)}")
        
        if input("¿Confirmar? (1. Sí / 2. No): ") == "1":
            self.permisos.append(Permiso(emp_id, tipo_id, f_desde, f_hasta, t_dh, tiempo, descuento))

    # --- MÉTODOS REQUERIDOS POR ICRUD ---
    def create(self): pass # Implementado arriba en métodos específicos
    def read(self):
        print("\n--- Lista de Empleados ---")
        for e in self.empleados: print(f"ID: {e.id} | {e.nombre}")
    def delete(self):
        id_del = int(input("ID a eliminar de empleados: "))
        self.empleados = list(filter(lambda x: x.id != id_del, self.empleados))

    # --- ESTADÍSTICAS CON FUNCIONES DE ORDEN SUPERIOR (HOF) ---
    def mostrar_estadisticas(self):
        self.clean_screen()
        # Uso de map, filter y reduce (o sum)
        total_emp = len(self.empleados)
        total_perm = len(self.permisos)
        
        remu = len(list(filter(lambda p: next(t.remunerado for t in self.tipos_permisos if t.id == p.tipo_id), self.permisos)))
        no_remu = total_perm - remu
        
        total_tiempo = sum(map(lambda p: p.tiempo, self.permisos))
        total_descuento = sum(map(lambda p: p.descuento, self.permisos))

        print("="*40 + "\n      ESTADÍSTICAS DE PERMISOS\n" + "="*40)
        print(f"Total empleados: {total_emp}")
        print(f"Total permisos: {total_perm}")
        print(f"Permisos remunerados: {remu}")
        print(f"Permisos no remunerados: {no_remu}")
        print(f"Total horas/días solicitados: {total_tiempo}")
        print(f"Monto total descontado: {self.format_money(total_descuento)}")
        input("\nPresione Enter para volver...")

# =========================================================
# 6. MENÚ PRINCIPAL
# =========================================================
def menu():
    sistema = SistemaPermisos()
    while True:
        print("\n--- SISTEMA DE GESTIÓN DE PERMISOS ---")
        print("1. Registrar Empleado")
        print("2. Registrar Tipo de Permiso")
        print("3. Registrar Permiso")
        print("4. Consultar Empleados")
        print("5. Ver Estadísticas")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1": sistema.create_empleado()
        elif opcion == "2": sistema.create_tipo_permiso()
        elif opcion == "3": sistema.create_permiso()
        elif opcion == "4": sistema.read()
        elif opcion == "5": sistema.mostrar_estadisticas()
        elif opcion == "6": break
        else: print("Opción no válida.")

if __name__ == "__main__":
    menu()