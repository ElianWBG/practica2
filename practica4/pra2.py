import os

# 1. DECORADOR (Para limpiar pantalla automáticamente en cada función)
def limpiar(func):
    def wrapper(*args, **kwargs):
        os.system('cls' if os.name == 'nt' else 'clear')
        return func(*args, **kwargs)
    return wrapper

# 2. MIXIN (Funciones que se "mezclan" en la clase principal)
class CalculadoraMixin:
    def sacar_valor_hora(self, sueldo):
        return round(sueldo / 240, 2)

    def sacar_descuento(self, tiempo, vh, es_remunerado, unidad):
        if es_remunerado == 'S': return 0.0
        # Si es Día (D) multiplicamos por 8 horas, si es Hora (H) por 1
        factor = 8 if unidad == 'D' else 1
        return round(tiempo * factor * vh, 2)

# 3. CLASES DE DATOS
class Empleado:
    def __init__(self, id, nom, sue, vh):
        self.id, self.nom, self.sue, self.vh = id, nom, sue, vh

class TipoPermiso:
    def __init__(self, id, desc, remu):
        self.id, self.desc, self.remu = id, desc, remu

class Permiso:
    def __init__(self, id, id_e, id_t, t_unidad, cant, desc):
        self.id, self.id_e, self.id_t = id, id_e, id_t
        self.t_unidad, self.cant, self.desc = t_unidad, cant, desc

# 4. CLASE PRINCIPAL
class Sistema(CalculadoraMixin):
    def __init__(self):
        self.empleados = []
        self.tipos = []
        self.permisos = []

    @limpiar
    def reg_empleado(self):
        print("=== REGISTRO EMPLEADO ===")
        nom = input("Nombre: ")
        sue = float(input("Sueldo: "))
        vh = self.sacar_valor_hora(sue)
        print(f"Valor Hora: ${vh}")
        if input("¿Guardar? (1.Si): ") == '1':
            new_id = len(self.empleados) + 1
            self.empleados.append(Empleado(new_id, nom, sue, vh))

    @limpiar
    def reg_tipo(self):
        print("=== TIPO DE PERMISO ===")
        desc = input("Descripción: ")
        rem = input("¿Remunerado? (S/N): ").upper()
        if input("¿Guardar? (1.Si): ") == '1':
            self.tipos.append(TipoPermiso(len(self.tipos) + 1, desc, rem))

    @limpiar
    def reg_permiso(self):
        print("=== REGISTRO PERMISO ===")
        id_e = int(input("ID Empleado: "))
        id_t = int(input("ID Tipo: "))
        
        # BUSQUEDA CON FUNCION DE ORDEN SUPERIOR (filter)
        emp = next(filter(lambda e: e.id == id_e, self.empleados), None)
        tip = next(filter(lambda t: t.id == id_t, self.tipos), None)

        if emp and tip:
            uni = input("Tipo (D/H): ").upper()
            can = float(input("Tiempo: "))
            desc_total = self.sacar_descuento(can, emp.vh, tip.remu, uni)
            
            print(f"Descuento: ${desc_total}")
            if input("¿Confirmar? (1.Si): ") == '1':
                self.permisos.append(Permiso(len(self.permisos)+1, id_e, id_t, uni, can, desc_total))
        else:
            print("Error: No existe empleado o tipo.")
            input("Presione Enter...")

    @limpiar
    def estadisticas(self):
        print("=== ESTADÍSTICAS ===")
        # FUNCIONES DE ORDEN SUPERIOR (map y filter)
        total_e = len(self.empleados)
        total_p = len(self.permisos)
        remu = len(list(filter(lambda x: x.desc == 0, self.permisos)))
        no_remu = total_p - remu
        total_desc = sum(map(lambda x: x.desc, self.permisos))

        print(f"Empleados: {total_e} | Permisos: {total_p}")
        print(f"Remunerados: {remu} | No Remu: {no_remu}")
        print(f"Total Descuentos: ${total_desc}")
        input("\nPresione Enter...")

# 5. MENU DE EJECUCION
def ejecutar():
    sis = Sistema()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Empleado\n2. Tipo Permiso\n3. Permiso\n4. Estadisticas\n5. Salir")
        op = input("Opción: ")
        if op == '1': sis.reg_empleado()
        elif op == '2': sis.reg_tipo()
        elif op == '3': sis.reg_permiso()
        elif op == '4': sis.estadisticas()
        elif op == '5': break

if __name__ == "__main__":
    ejecutar()