


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


#Definimos la funcion reporte detallado por mes

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
