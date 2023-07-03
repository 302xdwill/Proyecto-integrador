import funciones.registrar
import funciones.transferir
import funciones.listar 
import funciones.boletas
import funciones.deposito

usuarios = []

def salir():
    print("Saliendo del programa...")
    # Código para finalizar el programa

def main():
    while True:
        print("**..++..++..++..++..++..**")
        print("°========MONEY_HUB=======°")
        print("Tekito_tu_chosa           ")
        print("°========================°")
        print("| __*>>>>> MENÚ <<<<<*__ |")
        print("|1. registrar  personas  |")
        print("|2. Transferir dinero    |")
        print("|3. Listar usuarios      |")
        print("|4. Generar boletas      |")
        print("|5. depositar dinero     |")
        print("|6. Salir                |")
        print("°========================°")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            funciones.registrar.registrar_usuario(usuarios)
        elif opcion == "2":
            funciones.transferir.transferir_dinero(usuarios)
        elif opcion == "3":
            funciones.listar.listar_usuarios()
        elif opcion == "4":
            funciones.boletas.generar_pdf_transferencias()
        elif opcion == "5":
            funciones.deposito.depositar_dinero(usuarios)
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
    











