


#Definimos lista de categorias y lista de gastos

categorias = [
    "Gastos personales",
    "Estudio",
    "Trabajo",
    "Proyectos",
    "Necesidades básicas"
]

gastos = []


#Definimos la funcion registrar gasto

def registrar_gasto():
    print("\nREGISTRAR NUEVO GASTO")
    fecha = input("Ingresa la fecha (DD/MM/AAAA): ")
    descripcion = input("Ingresa la descripción del gasto: ")


    print("\nCategorías disponibles:")
    for i, categoria in enumerate(categorias, 1):
        print(f"{i}. {categoria}")
    opcion_categoria = input("Selecciona el número de la categoría: ")
    categoria = categorias[int(opcion_categoria) - 1]


    monto = float(input("Ingresa el monto del gasto: "))
    gasto = {
        "fecha": fecha,
        "descripcion": descripcion,
        "categoria": categoria,
        "monto": monto
    }
    gastos.append(gasto)
    print("\n¡Gasto registrado correctamente!")





#Definimos la funcion gastos por mes

def gastos_por_mes():
    print("\nGASTOS MENSUALES")
    mes = input("Ingresa el mes que deseas consultar en formato (MM): ")
    
    gastos_por_mes = []
    for gasto in gastos:
        if gasto["fecha"].split("/")[1] == mes:
            gastos_por_mes.append(gasto)


    if len(gastos_por_mes) == 0:
        print("\nNo tuviste gastos este mes :D")
    else:
        print(f"\nGastos que tuviste en el mes {mes}")
        for gasto in gastos_por_mes:
            print(f"{gasto['fecha']} | {gasto['descripcion']} | {gasto['categoria']} | ${gasto['monto']}")


#Definimos la funcion reporte detallado por mes.

def reporte_detallado_por_mes():
    print("\nREPORTE DETALLADO DEL MES")
    mes = input("Ingresa el mes que deseas consultar (Usa formato MM): ")
    
    total = 0
    gastos_por_mes = []
    for gasto in gastos:
        if gasto["fecha"].split("/")[1] == mes:
            gastos_por_mes.append(gasto)
            total += gasto["monto"]


    if len(gastos_por_mes) == 0:
        print("\nNo tuviste gastos este mes :D")
    else:
        print(f"\nResumen del mes {mes}")
        for gasto in gastos_por_mes:
            print(f"{gasto['fecha']} | {gasto['descripcion']} | {gasto['categoria']} | ${gasto['monto']}")
        print(f"\nTotal gastado en el mes {mes}: ${total}") 


def mostrar_menu():
    while True:
        print("\nMENU PRINCIPAL")
        print("1. Registrar gasto")
        print("2. Ver gastos por mes")
        print("3. Ver reporte del mes")
        print("4. Salir")
        
        opcion = input("\nSelecciona una opcion: ")
        
        if opcion == "1":
            registrar_gasto()
        elif opcion == "2":
            gastos_por_mes()
        elif opcion == "3":
            reporte_detallado_por_mes()
        elif opcion == "4":
            print("\nMuchas gracias por usar nuestros servicios. Son 50 lukas  :D")
            break
        else:
            print("\nOpcion no valida, ingresa un numero del 1 al 4 segun el menu :D")