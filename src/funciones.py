




categorias = [
    "Gastos personales",
    "Estudio",
    "Trabajo",
    "Proyectos",
    "Necesidades básicas"
]

lista_gastos = []



categorias = [
    "Gastos personales",
    "Estudio",
    "Trabajo",
    "Proyectos",
    "Necesidades básicas"
]

gastos = []

def registrar_gasto():
    print("\n--- REGISTRAR NUEVO GASTO ---")
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
    print("\n✅ Gasto registrado exitosamente!")