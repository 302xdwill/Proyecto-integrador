import os
import csv

def depositar_dinero(usuarios):
    # Obtener la ruta del archivo actual
    ruta_actual = os.path.dirname(os.path.abspath(__file__))

    # Ruta completa del archivo usuarios.csv
    ruta_usuarios = os.path.join(ruta_actual, "usuarios.csv")

    # Verificar si el archivo existe
    if not os.path.isfile(ruta_usuarios):
        print("No se encontró el archivo usuarios.csv.")
        return

    dni = input("Ingrese el DNI del usuario: ")
    monto = float(input("Ingrese el monto a depositar: "))

    usuario = None

    for u in usuarios:
        if u["DNI"] == dni:
            usuario = u
            break

    if not usuario:
        print("No se encontró un usuario con el DNI ingresado.")
        return

    usuario["Saldo"] += monto

    # Actualizar datos en archivo "usuarios.csv"
    actualizar_usuarios(usuarios)

    print(f"Depósito exitoso de {monto} unidades monetarias para el usuario {usuario['Nombre']}.")


def actualizar_usuarios(usuarios):
    # Obtener la ruta del archivo actual
    ruta_actual = os.path.dirname(os.path.abspath(__file__))

    # Ruta completa del archivo usuarios.csv
    ruta_usuarios = os.path.join(ruta_actual, "usuarios.csv")

    with open(ruta_usuarios, "w", newline="") as archivo_csv:
        writer = csv.DictWriter(archivo_csv, fieldnames=["DNI", "Nombre", "Saldo"])
        writer.writeheader()
        writer.writerows(usuarios)


# Ejemplo de uso

