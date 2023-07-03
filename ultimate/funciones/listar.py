import os
import csv

def listar_usuarios():
    # Obtener la ruta del archivo "listar.py"
    ruta_actual = os.path.dirname(os.path.abspath(__file__))

    # Generar la ruta completa para el archivo CSV
    ruta_csv = os.path.join(ruta_actual, "usuarios.csv")

    if not os.path.isfile(ruta_csv):
        print("El archivo CSV no existe. No hay usuarios registrados.")
        return

    with open(ruta_csv, "r") as archivo_csv:
        reader = csv.DictReader(archivo_csv)
        usuarios = list(reader)

        if not usuarios:
            print("No hay usuarios registrados.")
            return

        print("Usuarios registrados:")
        for i, usuario in enumerate(usuarios, start=1):
            print(f"{i}. Nombre: {usuario['Nombre']}, DNI: {usuario['DNI']}, Saldo: {usuario['Saldo']}")

if __name__ == "__main__":
    listar_usuarios()
