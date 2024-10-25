import random

VENTASPORDIA = [1, 5]
PRODUCTOS = [
    "LAMPARA DE TECHO",
    "LAMPARA DE PARED",
    "LAMPARA DE MESA",
    "LAMPARA DE PIE",
    "LUMINARIAS",
]
MODELOS = [1, 2, 3, 4]
PARAMETROS_ID = [1000, 9999]


def generarID(PARAMETROS_ID):
    id_cliente = random.randint(PARAMETROS_ID[0], PARAMETROS_ID[1])
    return id_cliente


def generarModelo(MODELOS):
    modelo = random.choice(MODELOS)
    return modelo


def generarProducto(PRODUCTOS):
    producto = random.choice(PRODUCTOS)
    return producto


def obtenerDia(mes, anio):
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Comprobamos si es un año bisiesto
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        dias_por_mes[1] = 29  # Si es bisiesto, febrero tiene 29 días

    return dias_por_mes[mes - 1]


def generarFecha(mes, anio):
    cantDias = obtenerDia(mes, anio)
    dia = random.randint(1, cantDias)

    fecha = [dia, mes, anio]

    return fecha


def generarVentas(VENTASPORDIA):
    cantVentas = random.choice(VENTASPORDIA)
    return cantVentas


def generarDatosDia(mes, anio):
    ventas = generarVentas(VENTASPORDIA)
    listaDatos = []

    for i in range(ventas):
        clienteId = generarID(PARAMETROS_ID)
        modelo = generarModelo(MODELOS)
        producto = generarProducto(PRODUCTOS)
        fecha = generarFecha(mes, anio)

        listaDatos.append([clienteId,producto,modelo, fecha])

    return listaDatos


def generarVentasMes(mes, anio):
    dias_del_mes = obtenerDia(mes, anio)
    ventas_mes = []

    for dia in range(1, dias_del_mes + 1):
        ventas_del_dia = generarDatosDia(mes, anio)
  
        for i in range(len(ventas_del_dia)):
            ventas_mes.append(ventas_del_dia[i])
    return ventas_mes


mes = 8 
anio = 2024
ventas_mes = generarVentasMes(mes, anio)

for venta in range(len(ventas_mes)):
    print(ventas_mes[venta])
