import os
import stat

def simulador_gestion_archivos():
    # 1. Definir nombres
    nombre_carpeta = "MiCarpetaDeber"
    nombre_archivo = os.path.join(nombre_carpeta, "notas.txt")

    print("--- Iniciando Simulación de Gestión de Archivos ---")

    # 2. Crear una carpeta (Simula mkdir())
    if not os.path.exists(nombre_carpeta):
        os.mkdir(nombre_carpeta)
        print(f"[ACCION] Carpeta '{nombre_carpeta}' creada con éxito.")
    else:
        print(f"[AVISO] La carpeta '{nombre_carpeta}' ya existe.")

    # 3. Crear y Escribir (Con manejo de excepciones para permisos)
    contenido = "Hola Ing. Jessica Cabezas, este es el contenido para el deber de Sistemas Operativos."
    
    try:
        with open(nombre_archivo, "w") as archivo:
            archivo.write(contenido)
            print(f"[ACCION] Archivo '{nombre_archivo}' creado/actualizado con éxito.")
    except PermissionError:
        print(f"[AVISO] El archivo tiene permisos de SOLO LECTURA. Restaurando permisos para escribir...")
        # Si da error de permiso, le devolvemos permiso de escritura temporalmente
        os.chmod(nombre_archivo, stat.S_IWRITE)
        with open(nombre_archivo, "w") as archivo:
            archivo.write(contenido)
        print(f"[ACCION] Archivo escrito tras restaurar permisos.")

    # 4. Leer el contenido (Simula open() y read())
    with open(nombre_archivo, "r") as archivo:
        lectura = archivo.read()
        print(f"[ACCION] Contenido leído: '{lectura}'")

    # 5. Cambiar permisos del archivo (Simula chmod())
    # S_IREAD es la constante para "Read Only"
    os.chmod(nombre_archivo, stat.S_IREAD)
    print(f"[ACCION] Permisos cambiados: Ahora el archivo es de SOLO LECTURA nuevamente.")

    print("\n--- Simulación Finalizada con éxito ---")

if __name__ == "__main__":
    simulador_gestion_archivos()