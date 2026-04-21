class BuclesEjemplo:
    def ejecutar(self):

        # =========================
        # WHILE
        # =========================
        print("=== WHILE ===")

        contador = 1

        while contador <= 3:
            print(f"Contador: {contador}")
            contador += 1

        # =========================
        # WHILE CON ELSE
        # =========================
        print("\n=== WHILE CON ELSE ===")

        numero = 1

        while numero < 3:
            print(numero)
            numero += 1
        else:
            print("Fin del while")

        # =========================
        # FOR CON RANGE
        # =========================
        print("\n=== FOR RANGE ===")

        for i in range(3):
            print(i)

        # =========================
        # FOR CON PASO
        # =========================
        print("\n=== FOR CON PASO ===")

        for i in range(0, 10, 2):
            print(i)

        # =========================
        # FOR CON LISTA
        # =========================
        print("\n=== FOR CON LISTA ===")

        frutas = ["manzana", "pera", "uva"]

        for fruta in frutas:
            print(fruta)

        # =========================
        # ENUMERATE
        # =========================
        print("\n=== ENUMERATE ===")

        for indice, fruta in enumerate(frutas):
            print(indice, fruta)

        # =========================
        # FOR CON DICCIONARIO
        # =========================
        print("\n=== FOR DICCIONARIO ===")

        persona = {"nombre": "Juan", "edad": 25}

        for clave, valor in persona.items():
            print(clave, valor)

        # =========================
        # BREAK
        # =========================
        print("\n=== BREAK ===")

        for i in range(5):
            if i == 3:
                break
            print(i)

        # =========================
        # CONTINUE
        # =========================
        print("\n=== CONTINUE ===")

        for i in range(5):
            if i == 2:
                continue
            print(i)

        # =========================
        # LIST COMPREHENSION
        # =========================
        print("\n=== LIST COMPREHENSION ===")

        cuadrados = [x**2 for x in range(4)]
        print(cuadrados)

        # =========================
        # DICCIONARIO COMPREHENSION
        # =========================
        print("\n=== DICT COMPREHENSION ===")

        cubos = {x: x**3 for x in range(4)}
        print(cubos)

        # =========================
        # EJERCICIO 1
        # =========================
        print("\n=== EJERCICIO 1 ===")

        for i in range(5):
            if i == 3:
                break
            print(i)

        # =========================
        # EJERCICIO 2
        # =========================
        print("\n=== EJERCICIO 2 ===")

        for i in range(5):
            if i == 2:
                continue
            print(i)

        # =========================
        # EJERCICIO 3 (ANÁLISIS)
        # =========================
        print("\n=== EJERCICIO 3 ===")

        resultado = [x for x in range(10) if x % 2 == 0]
        print(resultado)