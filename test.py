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
PARAMETROS_ID = [1, 20]
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

def calcularFacturacionPorCliente(ventas_mes):
    resumen_clientes = [] # POS[0][0]: ID CLIENTE | POS[0][1]: CANT VENTAS TOTALES | POS[0][2]: TOTAL FACTURADO 

    for i in range(len(ventas_mes)):
        venta = ventas_mes[i]
        cliente_id = venta[1]
        producto = venta[2]
        modelo = venta[3]
        precio = calcularPrecios(producto, modelo)

        cliente_existe = False
        for j in range(len(resumen_clientes)):
            if resumen_clientes[j][0] == cliente_id:
                resumen_clientes[j][1] += 1 
                resumen_clientes[j][2] += precio 
                cliente_existe = True
                break # Esto no me gusta
        
        if not cliente_existe:
            resumen_clientes.append([cliente_id, 1, precio]) 

    return resumen_clientes


def mostrarResumen(resumen_clientes):
    for i in range(len(resumen_clientes)):
        for j in range(i + 1, len(resumen_clientes)):
            if resumen_clientes[i][2] < resumen_clientes[j][2]:
                resumen_clientes[i], resumen_clientes[j] = resumen_clientes[j], resumen_clientes[i] # Esto tampoco me gusta

    print("Mes: Agosto 2024")
    print(f"{'ID cliente':<10} {'Total artículos':<15} {'Total facturado':<15}")
    for i in range(len(resumen_clientes)):
        cliente_id = resumen_clientes[i][0]
        total_articulos = resumen_clientes[i][1]
        total_facturado = resumen_clientes[i][2]
        print(f"{cliente_id:<10} {total_articulos:<15} ${total_facturado:<15}")


mes = 2 
anio = 2024
ventas_mes = generarDatosMes(mes, anio)

# De acá para abajo hay informacion para debuggear

print(ventas_mes)
for venta in ventas_mes: #Esto tiene que desaparecer, porque sino desapareceemos nosotros
    print(venta)


resumen_clientes = calcularFacturacionPorCliente(ventas_mes)
print()
print(resumen_clientes[0][2])
print()
for cliente in resumen_clientes:
    print(cliente)
print()
mostrarResumen(resumen_clientes)

"""
print(CalcularMesFacturado(ventas_mes))
print(ClientesUnicos(ventas_mes))
"""
