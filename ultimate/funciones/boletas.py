import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import csv

def generar_pdf_transferencias():
    # Obtener la ruta del archivo actual
    ruta_actual = os.path.dirname(os.path.abspath(__file__))

    # Ruta completa del archivo transferencias.csv
    ruta_transferencias = os.path.join(ruta_actual, "transferencias.csv")

    # Verificar si el archivo existe
    if not os.path.isfile(ruta_transferencias):
        print("No se encontró el archivo transferencias.csv.")
        return

    # Crear el archivo PDF
    nombre_pdf = "transferencias.pdf"
    ruta_pdf = os.path.join(ruta_actual, nombre_pdf)

    c = canvas.Canvas(ruta_pdf, pagesize=letter)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 700, "Transferencias Realizadas")
    c.setFont("Helvetica", 12)

    with open(ruta_transferencias, "r") as archivo_csv:
        reader = csv.reader(archivo_csv)
        next(reader)  # Saltar el encabezado

        y = 650  # Posición vertical inicial
        for row in reader:
            fecha = row[0]
            origen = row[1]
            destino = row[2]
            monto = row[3]

            texto = f"Fecha: {fecha}, Origen: {origen}, Destino: {destino}, Monto: {monto}"
            c.drawString(100, y, texto)
            y -= 20

    c.save()
    print(f"Se ha generado el archivo PDF: {nombre_pdf}")



