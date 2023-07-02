from persona import Persona
from producto import Producto
from venta import Venta
from venta_detalle import VentaDetalle
""" Clase que implementa persona"""

""" metodos que implementa persona"""
data_personas:list=[{"dni":"76606725",
                     "nombres":"Josue",
                     "apellidos":"Pastor",
                     "direccion":"sin direccion",
                     "telefono":"944501816" },
                    {"dni":"47259697",
                     "nombres":"Noe",
                     "apellidos":"Tipo",
                     "direccion":"direccion 1",
                     "telefono":"997124032" }]
personas:Persona=[]
def cargar_data_personas():
    for data in data_personas:
        personas.append(Persona(data["dni"],
                                data["nombres"],
                                data["apellidos"], 
                                data["direccion"], 
                                data["telefono"]))
    return personas

def insertar_persona():
    dni:str = input("Ingrese el DNI de la Persona: ")
    nombres:str = input("Ingrese nombres de la Persona: ")
    apellidos:str = input("Ingrese apellidos de la Persona: ")
    direccion:str = input("Ingrese direccion de la Persona: ")
    telefono:str = input("Ingrese telefono de la Persona: ")
    personas.append(Persona(dni,nombres,apellidos,direccion,telefono))
    return personas

def listar_personas():
    for persona in personas:
        print(persona.convertir_a_string())

def buscar_persona():
    dni:str= input("Ingrese el DNI de la Persona: ")
    for persona in personas:
        if persona.dni==dni:
            print(persona.convertir_a_string())
            return persona
        
def editar_persona():
    dni:str = input("Ingrese el Dni de la Persona: ")
    for persona in personas:
        if persona.dni == dni:
            print(persona.convertir_a_string())
            persona.nombres = input("Ingrese nombres de la Persona: ")
            persona.apellidos = input("Ingrese apellidos de la Persona: ")
            persona.direccion = input("Ingrese direccion de la Persona: ")
            persona.telefono = input("Ingrese telefono de la Persona: ")
        break
def eliminar_persona():
    dni:str= input("Ingrese el Dni de la Persona: ")
    for indice, persona in enumerate(personas):
        if persona.dni== dni:
            print(persona.convertir_a_string())
            personas.pop(indice)
        break

""" metodos que implementa producto"""
data_productos:list=[{"codigo":"001","nombre":"pan", "precio":1.00},
                     {"codigo":"002","nombre":"empanada", "precio":2.00}]
productos:Producto=[]
def cargar_data_productos():
    for data in data_productos:
        productos.append(Producto(data["codigo"],
                                  data["nombre"], 
                                  data["precio"]))
    return productos


def insertar_producto():
    codigo:str = input("Ingrese el Codigo del producto: ")
    nombre:str = input("Ingrese nombre  del  producto: ")
    precio:str = input("Ingrese precio del producto: ")
    
    productos.append(Producto(codigo,nombre,precio))
    return productos

def listar_producto():
    for producto in productos:
        print(producto.convertir_a_string())

def buscar_producto():
    codigo:str= input("Ingrese codigo del producto: ")
    for prooducto in productos:
        if prooducto.codigo==codigo:
            print(prooducto.convertir_a_string())
            return prooducto
        
def editar_producto():
    codigo:str= input("Ingrese codigo del producto: ")
    for producto in productos:
        if producto.codigo==codigo:
            print(producto.convertir_a_string())
            producto.nombre = input("Ingrese nombre  del  producto: ")
            producto.precio = input("Ingrese precio del producto: ")
            
        break
def eliminar_persona():
    codigo:str= input("Ingrese codigo del producto: ")
    for indice, producto in enumerate(productos):
        if producto.codigo==codigo:
            print(producto.convertir_a_string())
            productos.pop(indice)
        break

ventas:Venta=[]
venta_detalles:VentaDetalle=[]
def agregar_productos():
    producto=buscar_producto()
    venta_detalles.append(VentaDetalle(len(venta_detalles)+1, producto.codigo,producto.nombre,1,1))
    for venta_detalle in venta_detalles:
        print(venta_detalle.convertir_a_string())


def insertar_venta():
    cliente:Persona=buscar_persona()
    numero=len(ventas)+1
    continuar_agregando_producto:bool=True
    while continuar_agregando_producto:
        opcion:str=input("1 para agregar producto y 2 para no agregar mas productos: ")
        match opcion:
            case "1":
                agregar_productos()
            case "2":
                #for venta_detalle in venta_detalles:
                #    print(venta_detalle.codigo)
                continuar_agregando_producto=False
    
    






def menu_texto():
    print("===========MENU==========")
    print("1: para insertar persona: ")
    print("2: para listar personas: ")
    print("3: para buscar persona: ")
    print("4: para editar persona: ")
    print("5: para eliminar  persona: ")

    print("6: para insertar producto: ")
    print("7: para listar  productos: ")
    print("8: para buscar producto: ")
    print("9: para editar producto: ")
    print("10: para eliminar  producto: ")

    print("11: para insertar venta: ")

    print("30: para salir: ")
    return True

def menu():
    contunuar:bool= True
    while contunuar:
        menu_texto()
        opcion:str= input("seleccione la opcion: ")

        match opcion:
            case "1":
                insertar_persona()
            case "2":
                listar_personas()
            case "3":
                buscar_persona()
            case "4":
                editar_persona()
            case "5": 
                eliminar_persona()

            case "6":
                insertar_producto()
            case "7":
                listar_producto()
            case "8":
                buscar_producto()
            case "9":
                editar_producto()
            case "10": 
                eliminar_persona()
            case "11": 
                insertar_venta()
            case "30":
                contunuar=False

def main():
    cargar_data_personas()
    cargar_data_productos()
    print("Inicia el programa")
    menu()
    return True

if __name__ == "__main__":
    main()
