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

def calcularPrecios(producto,modelo):
    valorFinal = 0
    if (producto == "LAMPARA DE TECHO"):
        if(modelo == 1):
            valorFinal = 45000
        elif(modelo == 2):
            valorFinal = 60000
        elif(modelo == 3):
            valorFinal = 88000
        elif(modelo == 4):
            valorFinal = 100000
    elif (producto == "LAMPARA DE PARED"):
        if(modelo == 1):
            valorFinal = 23500
        elif(modelo == 2):
            valorFinal = 44000
        elif(modelo == 3):
            valorFinal = 64000
        elif(modelo == 4):
            valorFinal = 85000
    elif (producto == "LAMPARA DE MESA"):
        if(modelo == 1):
            valorFinal = 20000
        elif(modelo == 2):
            valorFinal = 25000
        elif(modelo == 3):
            valorFinal = 28000
        elif(modelo == 4):
            valorFinal = 30000
    elif (producto == "LAMPARA DE PIE"):
        if(modelo == 1):
            valorFinal = 35000
        elif(modelo == 2):
            valorFinal = 40000
        elif(modelo == 3):
            valorFinal = 43000
        elif(modelo == 4):
            valorFinal = 50000
    elif (producto == "LUMINARIAS"):
        if(modelo == 1):
            valorFinal = 2100
        elif(modelo == 2):
            valorFinal = 3200
        elif(modelo == 3):
            valorFinal = 3800
        elif(modelo == 4):
            valorFinal = 4800
    return valorFinal
            
            



def obtenerDias(mes, anio):
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Comprobamos si es un año bisiesto
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        dias_por_mes[1] = 29  # Si es bisiesto, febrero tiene 29 días

    return dias_por_mes[mes - 1]


def generarMes(mes, anio):

    diasDelMes = []

    for i in range(obtenerDias(mes, anio)):
        
        dia = (i + 1)
        diasDelMes.append(dia)
        
    return diasDelMes


def generarVentas(VENTASPORDIA):
    cantVentas = random.randint(VENTASPORDIA[0],VENTASPORDIA[1])
    return cantVentas


def generarDatosMes(mes, anio):
    listaDatos = []
    fechas = generarMes(mes,anio)

    for dia in range(len(fechas)):
        ventas = generarVentas(VENTASPORDIA)
 
        for i in range(ventas):
            clienteId = generarID(PARAMETROS_ID)
            modelo = generarModelo(MODELOS)
            producto = generarProducto(PRODUCTOS)
        

            listaDatos.append([fechas[dia],clienteId,producto,modelo])

    return listaDatos


mes = 2 
anio = 2024
ventas_mes = generarDatosMes(mes, anio)


for venta in range(len(ventas_mes)):
    vendido = ventas_mes[venta]
    print(vendido)
    print("$",calcularPrecios(vendido[2],vendido[3]))
    


