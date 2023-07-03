import os
import csv


def registrar_usuario(usuarios):
    dni = input("Ingrese el DNI del usuario: ")
    nombre = input("Ingrese el nombre del usuario: ")
    saldo = float(input("Ingrese el saldo del usuario: "))

    usuario = {"DNI": dni, "Nombre": nombre, "Saldo": saldo}
    usuarios.append(usuario)
    print("Usuario registrado con éxito.")

    # Obtener la ruta del archivo "registrar.py"
    ruta_actual = os.path.dirname(os.path.abspath(__file__))

    # Generar la ruta completa para el archivo CSV
    ruta_csv = os.path.join(ruta_actual, "usuarios.csv")

    if os.path.exists(ruta_csv):
        # Actualizar el archivo CSV existente
        with open(ruta_csv, "a", newline="") as archivo_csv:
            writer = csv.DictWriter(archivo_csv, fieldnames=["DNI", "Nombre", "Saldo"])
            writer.writerow(usuario)
    else:
        # Crear un nuevo archivo CSV
        with open(ruta_csv, "w", newline="") as archivo_csv:
            writer = csv.DictWriter(archivo_csv, fieldnames=["DNI", "Nombre", "Saldo"])
            writer.writeheader()
            writer.writerow(usuario)
    
    print("Archivo CSV actualizado o generado con los usuarios registrados.")
