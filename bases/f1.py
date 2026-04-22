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
        print(f" {self.id}--{self.id_empleado}-- {self.id_tipo_permiso}--{self.fecha_desde}--{self.fecha_hasta}--{self.tipo}--{self.tiempo} " )
        return




p=empleado("elian",560)
p.mostrar_info()
t1 = tipo_permiso("Enfermedad", "S")
t2 = tipo_permiso("Personal", "N")
t1.mostrar_info()
t2.mostrar_info()
per1 = permiso(1, 1, "2024-01-15", "2024-01-17", "D", 2)
per1.mostrar_info()
        
        
        
        