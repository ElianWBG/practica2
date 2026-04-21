
#funcion con sin retorno
def saludar():
    print("\n---1----\n")
    print("hola mundito")
saludar()
#funcion para sumar con retorno
def sumar(a,b):
  
    return a * b
print("\n---2----\n")
print(sumar(4,21))
#funcion retorno establecida
def presentarse(nombre,edad=24):
    return f"{nombre} tiene la edad de {edad}"
print("\n---3----\n")
print(presentarse("predro"))
print(presentarse("juan",46))
#args sirven como parametro para sumar bastantes datos o operaciones con ellos
print("\n---4----\n")
def sumar_datos(*datos):
    return sum(datos)
print(sumar_datos(1,2))
#arg multiplicacion
def multiplicar(*args):
    total = 1
    for numero in args:
        total*= numero
    return total
print(multiplicar(2, 3))
#los kwargs son diccionarios donde se puede meter clave y valor donde el nombre seria clave
# y valor seria el texto o valor asignado
print("\n---5----\n")
def mostrar_datos(**datos):
    for clave, valor in datos.items():
        print(clave,valor)
mostrar_datos(nombre="elian",edad=34)
# lambda es una funcion pequeñita 
print("\n---6----\n")
cuadrado=lambda x: x**2
print(cuadrado(4))
print("\n---7----\n")
#retorno multiple se utiliza para retornar varios datos utilizamos en el return las operaciones y abajo las definimos 
# y igualamos al nombre de la funcion dentro su operacion
def division(a,b):
    return a/b, a%b
cociente,resto=division(10,2)
print(cociente, resto)
#recursividad
#funcion se llama asi misma dentro de ella
print("\n---8----\n")
def factorial(n):
    if n==0:
        return 1
    return n* factorial(n-1)
print(factorial(6))


   