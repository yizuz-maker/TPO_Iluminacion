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
PARAMETROS_ID = [1000, 2000]
PRECIO_LAMP_TECHO=[45000,60000,80000,100000]
PRECIO_LAMP_PARED=[23500,44000,64000,85000]
PRECIO_LAMP_MESA=[20000,25000,28000,30000]
PRECIO_LAMP_PIE=[35000,40000,43000,50000]
PRECIO_LUMINARIA=[2100,3200,3800,4800] 


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
       valorFinal = PRECIO_LAMP_TECHO[modelo-1]
    elif (producto == "LAMPARA DE PARED"):
        valorFinal = PRECIO_LAMP_PARED[modelo-1]
    elif (producto == "LAMPARA DE MESA"):
       valorFinal = PRECIO_LAMP_MESA[modelo-1]
    elif (producto == "LAMPARA DE PIE"):
       valorFinal = PRECIO_LAMP_PIE[modelo-1]
    elif (producto == "LUMINARIAS"):
       valorFinal = PRECIO_LUMINARIA[modelo-1]
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


def CalcularMesFacturado(ventasMes):
    totalFacturado = 0
    ventasTotales = len(ventas_mes)
    totalCosto = 0
    for i in range(ventasTotales):
        venta = ventasMes[i]
        valorVenta= calcularPrecios(venta[2],venta[3])
        totalFacturado += valorVenta
        totalCosto += calcularCostoProducto(venta)
    return totalFacturado,ventasTotales,totalCosto


def ClientesUnicos(ventasMes):
    ventasTotales = len(ventas_mes)
    clientesUnicos = []
    for i in range(ventasTotales):
        venta = ventasMes[i]
        clienteExiste = False
        for j in range(len(clientesUnicos)):
            if venta[1] == clientesUnicos[j]:
                clienteExiste = True      
        if not clienteExiste:
            clientesUnicos.append(venta[1])
    return len(clientesUnicos)

def calcularCostoProducto(vendido):
    precio = calcularPrecios(vendido[2],vendido[3])
    return precio // 2

mes = 2 
anio = 2024
ventas_mes = generarDatosMes(mes, anio)

print(CalcularMesFacturado(ventas_mes))
print(ClientesUnicos(ventas_mes))

