def decorador_interfaz(titulo):          # (1) Función externa — recibe el título
    def wrapper(func):                   # (2) Función media — recibe la función a decorar
        def inner(*args, **kwargs):      # (3) Función interna — es lo que realmente se ejecuta
            print("=" * 40)
            print(f"{titulo.center(40)}")  # Imprime el título centrado
            print("=" * 40)
            res = func(*args, **kwargs)    # Llama a la función original
            return res
        return inner
    return wrapper

def con_separador(func):
    def envoltura(*args):
        print("----------")
        func(*args)
        print("----------")
    return envoltura
@con_separador
def saludar(nombre):
    print(f"Hola, {nombre}! ")

@con_separador
def despedir(nombre):
    print(f"Adios, {nombre}!")

saludar("Ana")
despedir("Ana")


