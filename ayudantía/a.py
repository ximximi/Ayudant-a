cargos = ["CEO", "Analista", "Desarrollador"]
trabajadores = []


def menu_principal():
    while True:
        print ("Menú principal:\n1. Registrar trabajador\n2. Listar los todos los trabajadores\n3. Imprimir planilla de sueldos\n4. Salir")
        opc = input("Ingrese una opción:")
        if opc == "1":
            print("1. Registrar trabajador")
            registrar_tra()
        elif opc == "2":
            print("2. Listar los todos los trabajadores")
            listar_tra()

        elif opc == "3":
            print("3. Imprimir planilla de sueldos")
            imprimir_info()
        elif opc =="4":
            break





def registrar_tra():
    nombre = input("Ingrese nombre del trabajador: ")
    apellido = input ("Ingrese apellido del trabajador: ")
    cargo = input ("Ingrese cargo: ")
    sueldo_br = int(input("Ingrese sueldo bruto: "))

    while cargo not in cargos:
        print ("No se encuentra en la lista")
    try:
        sueldo_br = int(input("Ingrese sueldo bruto: "))
    except ValueError:
        print("Ingrese un valor entero")

    trabajador = {
        "nombre": nombre,
        "apellido": apellido,
        "cargo": cargo,
        "sueldo": sueldo_br
    }
    trabajadores.append(trabajador)

def listar_tra():
    if not trabajadores:
        print ("No hay trabajadores :(")
    else:
        for trabajador in trabajadores:
            print (f"Nombre: {trabajador["nombre"]}", f"Apellido: {trabajador["apellido"]}", f"Cargo: {trabajador["cargo"]}")
            #prueba a ver si se puede con {trabajador[0]}

def imprimir_info():
    print ("Opciones de impresión: \n1. Imprimir todos los trabajadores\n2. Imprimir por cargo específico")
    opcion = input ("Seleccione una opción:")
    if opcion == "1":
        print("a")
    


    #write y print, lo mismo
        
def agregar_cargo():
    nuevo_car = input ("Ingrese un nuevo cargo")
    if nuevo_car not in cargos:
        print ("")




menu_principal()

#El strip sirve para borrar los espacios del input, porque los espacios igual se toman en cuenta
#revisar: not in, try except, append


#st.parra@profesor.duoc.cl