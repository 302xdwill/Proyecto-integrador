"""
import os
import csv
from datetime import datetime

def transferir_dinero(usuarios):
    if len(usuarios) < 2:
        print("No hay suficientes usuarios registrados para transferir dinero.")
        return
    
    print("Usuarios registrados:")
    for i, usuario in enumerate(usuarios):
        print(f"{i+1}. {usuario['Nombre']} (DNI: {usuario['DNI']})")

    dni_origen = input("Ingrese el DNI del usuario de origen: ")
    dni_destino = input("Ingrese el DNI del usuario de destino: ")
    monto = float(input("Ingrese el monto a transferir: "))

    usuario_origen = None
    usuario_destino = None

    for usuario in usuarios:
        if usuario["DNI"] == dni_origen:
            usuario_origen = usuario
        elif usuario["DNI"] == dni_destino:
            usuario_destino = usuario

    if not usuario_origen or not usuario_destino:
        print("No se encontraron usuarios con los DNIs ingresados.")
        return

    if usuario_origen["Saldo"] < monto:
        print("El usuario de origen no tiene suficiente saldo para realizar la transferencia.")
        return

    usuario_origen["Saldo"] -= monto
    usuario_destino["Saldo"] += monto

    # Actualizar datos en archivo "usuarios.csv"
    actualizar_usuarios(usuarios)

    # Registrar la transferencia en otro archivo CSV
    registrar_transferencia(usuario_origen, usuario_destino, monto)

    print(f"Transferencia exitosa de {monto} unidades monetarias de {usuario_origen['Nombre']} a {usuario_destino['Nombre']}.")


def actualizar_usuarios(usuarios):
    # Obtener la ruta del archivo "transferir.py"
    ruta_actual = os.path.dirname(os.path.abspath(__file__))

    # Generar la ruta completa para el archivo CSV "usuarios.csv"
    ruta_csv = os.path.join(ruta_actual, "usuarios.csv")

    with open(ruta_csv, "w", newline="") as archivo_csv:
        writer = csv.DictWriter(archivo_csv, fieldnames=["DNI", "Nombre", "Saldo"])
        writer.writeheader()
        writer.writerows(usuarios)


def registrar_transferencia(usuario_origen, usuario_destino, monto):
    # Obtener la ruta del archivo "transferir.py"
    ruta_actual = os.path.dirname(os.path.abspath(__file__))

    # Generar la ruta completa para el archivo CSV "transferencias.csv"
    ruta_transferencias = os.path.join(ruta_actual, "transferencias.csv")

    # Obtener la fecha y hora actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Crear una lista con los datos de la transferencia
    transferencia = [fecha_actual, usuario_origen["DNI"], usuario_destino["DNI"], monto]

    # Verificar si el archivo "transferencias.csv" ya existe
    archivo_existente = os.path.isfile(ruta_transferencias)

    with open(ruta_transferencias, "a", newline="") as archivo_csv:
        writer = csv.writer(archivo_csv)

        # Si el archivo no existe, escribir el encabezado
        if not archivo_existente:
            writer.writerow(["Fecha", "Origen", "Destino", "Monto"])

        # Escribir los datos de la transferencia en el
"""



import os
import csv
from datetime import datetime

def transferir_dinero(usuarios):
    if len(usuarios) < 2:
        print("No hay suficientes usuarios registrados para transferir dinero.")
        return
    
    print("Usuarios registrados:")
    for i, usuario in enumerate(usuarios):
        print(f"{i+1}. {usuario['Nombre']} (DNI: {usuario['DNI']}) (Saldo: {usuario['Saldo']})")

    dni_origen = input("Ingrese el DNI del usuario de origen: ")
    dni_destino = input("Ingrese el DNI del usuario de destino: ")
    monto = float(input("Ingrese el monto a transferir: "))

    usuario_origen = None
    usuario_destino = None

    for usuario in usuarios:
        if usuario["DNI"] == dni_origen:
            usuario_origen = usuario
        elif usuario["DNI"] == dni_destino:
            usuario_destino = usuario

    if not usuario_origen or not usuario_destino:
        print("No se encontraron usuarios con los DNIs ingresados.")
        return

    if usuario_origen["Saldo"] < monto:
        print("El usuario de origen no tiene suficiente saldo para realizar la transferencia.")
        return

    usuario_origen["Saldo"] -= monto
    usuario_destino["Saldo"] += monto

    # Actualizar datos en archivo "usuarios.csv"
    actualizar_usuarios(usuarios)

    # Registrar la transferencia en el archivo CSV "transferencias.csv"
    registrar_transferencia(usuario_origen, usuario_destino, monto)

    print(f"Transferencia exitosa de {monto} unidades monetarias de {usuario_origen['Nombre']} a {usuario_destino['Nombre']}.")

    # Imprimir boleta de transferencia
    imprimir_boleta(usuario_origen, usuario_destino, monto)


def actualizar_usuarios(usuarios):
    # Obtener la ruta del archivo "transferir.py"
    ruta_actual = os.path.dirname(os.path.abspath(__file__))

    # Generar la ruta completa para el archivo CSV "usuarios.csv"
    ruta_csv = os.path.join(ruta_actual, "usuarios.csv")

    with open(ruta_csv, "w", newline="") as archivo_csv:
        writer = csv.DictWriter(archivo_csv, fieldnames=["DNI", "Nombre", "Saldo"])
        writer.writeheader()
        writer.writerows(usuarios)


def registrar_transferencia(usuario_origen, usuario_destino, monto):
    # Obtener la ruta del archivo "transferir.py"
    ruta_actual = os.path.dirname(os.path.abspath(__file__))

    # Generar la ruta completa para el archivo CSV "transferencias.csv"
    ruta_transferencias = os.path.join(ruta_actual, "transferencias.csv")

    # Obtener la fecha y hora actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Verificar si el archivo "transferencias.csv" ya existe
    archivo_existente = os.path.isfile(ruta_transferencias)

    with open(ruta_transferencias, "a", newline="") as archivo_csv:
        writer = csv.writer(archivo_csv)

        # Si el archivo no existe, escribir el encabezado
        if not archivo_existente:
            writer.writerow(["Fecha", "Origen", "Destino", "Monto"])

        # Escribir los datos de la transferencia en el archivo
        writer.writerow([fecha_actual, usuario_origen["DNI"], usuario_destino["DNI"], monto])


def imprimir_boleta(usuario_origen, usuario_destino, monto):
    print("\n====== BOLETA DE TRANSFERENCIA ======")
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Usuario de origen: {usuario_origen['Nombre']} (DNI: {usuario_origen['DNI']})")
    print(f"Usuario de destino: {usuario_destino['Nombre']} (DNI: {usuario_destino['DNI']})")
    print(f"Monto transferido: {monto}")
    print("====================================")
