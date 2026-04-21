class UnpackingEjemplo:
    def ejecutar(self):

        print("=== UNPACKING ===")

        # =========================
        # UNPACKING BÁSICO
        # =========================
        print("\n=== UNPACKING BÁSICO ===")

        numeros = [1, 2]
        a, b = numeros

        print("a =", a)
        print("b =", b)

        # =========================
        # UNPACKING EXTENDIDO
        # =========================
        print("\n=== UNPACKING EXTENDIDO ===")

        lista = [1, 2, 3, 4, 5]
        primero, *resto, ultimo = lista

        print("Primero:", primero)
        print("Resto:", resto)
        print("Último:", ultimo)

        # =========================
        # UNPACKING EN DICCIONARIOS
        # =========================
        print("\n=== UNPACKING DE DICCIONARIOS ===")

        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3, "d": 4}

        dict_combinado = {**dict1, **dict2}

        print(dict_combinado)

        # =========================
        # UNPACKING EN FUNCIONES
        # =========================
        print("\n=== UNPACKING EN FUNCIONES ===")

        def suma(a, b, c):
            return a + b + c

        numeros = [1, 2, 3]
        resultado = suma(*numeros)

        print("Resultado:", resultado)

        # =========================
        # UNPACKING EN BUCLES
        # =========================
        print("\n=== UNPACKING EN BUCLES ===")

        coordenadas = [(1, 2), (3, 4), (5, 6)]

        for x, y in coordenadas:
            print("x =", x, ", y =", y)

        # =========================
        # EJERCICIO 1
        # =========================
        print("\n=== EJERCICIO 1 ===")

        datos = [10, 20]
        x, y = datos

        print(x)
        print(y)

        # =========================
        # EJERCICIO 2
        # =========================
        print("\n=== EJERCICIO 2 ===")

        valores = [100, 200, 300, 400]
        primero, *medio, ultimo = valores

        print("Primero:", primero)
        print("Medio:", medio)
        print("Último:", ultimo)

        # =========================
        # EJERCICIO 3 (ANÁLISIS)
        # =========================
        print("\n=== EJERCICIO 3 ===")

        def multiplicar(a, b, c):
            return a * b * c

        numeros = [2, 3, 4]
        print(multiplicar(*numeros))
objeto_unpacking = UnpackingEjemplo()
objeto_unpacking.ejecutar()