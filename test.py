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


def CalcularMesFacturado(ventas_mes):
    totalFacturado = 0
    ventasTotales = len(ventas_mes)
    totalCosto = 0
    for i in range(ventasTotales):
        venta = ventas_mes[i]
        valorVenta= calcularPrecios(venta[2],venta[3])
        totalFacturado += valorVenta
        totalCosto += calcularCostoProducto(venta)
    return totalFacturado,ventasTotales,totalCosto


def ClientesUnicos(ventas_mes):
    ventasTotales = len(ventas_mes)
    clientesUnicos = []
    for i in range(ventasTotales):
        venta = ventas_mes[i]
        clienteExiste = False
        for j in range(len(clientesUnicos)):
            if venta[1] == clientesUnicos[j]:
                clienteExiste = True      
        if not clienteExiste:
            clientesUnicos.append(venta[1])
    return len(clientesUnicos)

def mostrarTotalMes(ventas_mes, mes, anio):
    totalFacturado,ventasTotales,totalCosto = CalcularMesFacturado(ventas_mes)
    clientesUnicos = ClientesUnicos(ventas_mes)
    print("Opcion 1: Totales Mes\n")
    print(f"Mes: {mes} {anio}\n")
    print(f"Total Facturado: ${totalFacturado}")
    print(f"Total ventas realizadas: {ventasTotales}")
    print(f"Total cliente unicos: {clientesUnicos}")
    print(f"Total Costo adquisición productos vendidos: ${totalCosto}")
    
    
    


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
        j = 0
        while (not cliente_existe) and (j < len(resumen_clientes)):
            
            if resumen_clientes[j][0] == cliente_id:
                resumen_clientes[j][1] += 1 
                resumen_clientes[j][2] += precio 
                cliente_existe = True
            j += 1 
            
        
        if not cliente_existe:
            resumen_clientes.append([cliente_id, 1, precio]) 

    return resumen_clientes


def mostrarResumen(resumen_clientes):
    for i in range(len(resumen_clientes)):
        for j in range(i + 1, len(resumen_clientes)):
            if resumen_clientes[i][2] < resumen_clientes[j][2]: # Esta logica es para ordenar como se muestran las cosas en el print (algo no muy importante)
                resumen_clientes[i], resumen_clientes[j] = resumen_clientes[j], resumen_clientes[i] # Esto tampoco me gusta

    print("Mes: Agosto 2024")
    print(f"{'ID cliente':<10} {'Total artículos':<15} {'Total facturado':<15}")
    for i in range(len(resumen_clientes)):
        cliente_id = resumen_clientes[i][0]
        total_articulos = resumen_clientes[i][1]
        total_facturado = resumen_clientes[i][2]
        print(f"{cliente_id:<10} {total_articulos:<15} ${total_facturado:<15}")

def mostrarDetalleDelDia(ventas_mes, dia):
    resultado = []
    for i in range(len(ventas_mes)):
        if ventas_mes[i][0] == dia:
            resultado.append([ventas_mes[i][1], ventas_mes[i][2], ventas_mes[i][3], calcularPrecios(ventas_mes[i][2], ventas_mes[i][3])])
    return resultado

def mostrarDetallePorDia(ventas_mes): 
    resultado_por_dia = [] 
    contador = 0
    acumulador = 0
    for i in range(len(ventas_mes)):
       
        if i != len(ventas_mes) - 1: 
            if ventas_mes[i][0] == ventas_mes[i+1][0]:
                contador += 1
                acumulador += calcularPrecios(ventas_mes[i][2], ventas_mes[i][3])
            else:
                ultima_venta = calcularPrecios(ventas_mes[i][2], ventas_mes[i][3])
                resultado_por_dia.append([ventas_mes[i][0],contador+1, acumulador + ultima_venta])
                contador = 0 
                acumulador = 0
        else: 
            acumulador += calcularPrecios(ventas_mes[i][2], ventas_mes[i][3])
            resultado_por_dia.append([ventas_mes[i][0],contador+1, acumulador])
            
    return resultado_por_dia

def seleccionarProducto():
    print("1.........Lampara de Techo")
    print("2.........Lampara de Pared")
    print("3.........Lampara de Mesa")
    print("4.........Lampara de Pie")
    print("5.........Luminarias")

    opcion = int(input("Seleccione un producto: "))
    if opcion >= 1 and opcion <= 5:
        return PRODUCTOS[opcion - 1]
    else:
        return None
    
def totalPorProductoYModelo(ventas_mes, producto_seleccionado):
    # Filtrar ventas por el producto seleccionado
    ventas_filtradas = []
    for i in range(len(ventas_mes)):
        if ventas_mes[i][2] == producto_seleccionado:
            ventas_filtradas.append(ventas_mes[i])

    if not ventas_filtradas:
        print(f"No se encontraron ventas para el producto seleccionado")
        return None

    total_facturado = 0
    total_ventas = 0
    ventas_por_modelo = [0, 0, 0, 0]  # Contadores para modelos 1, 2, 3, y 4
    clientes_unicos = []  # Lista para almacenar los clientes únicos
    total_costo = 0

    for i in range(len(ventas_filtradas)):
        venta = ventas_filtradas[i]
        modelo = venta[3]
        cliente_id = venta[1]
        precio = calcularPrecios(venta[2], modelo)
        costo = calcularCostoProducto(venta)

        # Sumar al total facturado y costo
        total_facturado += precio
        total_costo += costo
        total_ventas += 1

        # Incrementar el contador del modelo correspondiente
        ventas_por_modelo[modelo - 1] += 1

        # Verificar si el cliente es único`
        cliente_existe = False
        for j in range(len(clientes_unicos)):
            if clientes_unicos[j] == cliente_id:
                cliente_existe = True
        if not cliente_existe:
            clientes_unicos.append(cliente_id)
            
        return[producto_seleccionado, total_facturado, total_ventas, ventas_por_modelo, len(clientes_unicos), total_costo]

def mostrarTotalPorProductoYModelo(ventas_mes, mes, anio):
    producto_seleccionado = seleccionarProducto()
    total = totalPorProductoYModelo(ventas_mes, producto_seleccionado)
    if total is not None:
        print("Opcion 2: Total por tipo de Producto y modelo.\n")
        print(f"Mes: {mes} {anio}\n")
        print(f"Producto seleccionado: {total[0]}\n")
        
        print(f"Total facturado: ${total[1]}")
        print(f"Total ventas realizadas: {total[2]}")
        print(f"\t Total ventas realizadas modelo 1: {total[3][0]}")
        print(f"\t Total ventas realizadas modelo 2: {total[3][1]}")
        print(f"\t Total ventas realizadas modelo 3: {total[3][2]}")
        print(f"\t Total ventas realizadas modelo 4: {total[3][3]}")
        print(f"Total Clientes Unicos: {total[4]}")
        print(f"Total Costo adquisición productos vendidos: ${total[5]}")
  
def mostrarOpcionesMenu():
    print("ILUMINACION")
    print("------------------")
    print("1...............Opcion 1: Totales Mes")
    print("2...............Opcion 2: Total por tipo de Producto y modelo")
    print("3...............Opcion 3: Detalle por Clientes")
    print("4...............Opcion 4: Detalle por día")
    print("5...............Opcion 5: Detalle del día")
    print("6...............Opcion 6: SALIR")

def menu(ventas_mes, mes, anio):
    bandera = True
    while bandera:
        mostrarOpcionesMenu() 
        opcion = int(input("Ingrese una opcion: "))
        if (opcion >= 1 and opcion <= 6):
            if opcion == 1:
                mostrarTotalMes(ventas_mes,mes, anio)
            elif opcion == 2: 
                mostrarTotalPorProductoYModelo(ventas_mes,mes, anio)
            
            elif opcion == 6:
                bandera = False
                print("Saliendo del programa...")
            else: 
                print("Ha ocurrido un error")
        else: 
            print("Ingrese una opcion válida")
    

def ingresarMesyAnio():
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))
    if mes>= 1 and mes <= 12:
        return [mes, anio]
    else: 
        return None

def main():
    datos = ingresarMesyAnio()
    if datos is not None: 
        mes = datos[0]
        anio = datos[1]
        ventas_mes = generarDatosMes(mes, anio)
        menu(ventas_mes, mes, anio)
    else: 
        print("Ingrese un mes correcto")


main()
# De acá para abajo hay informacion para debuggear
"""
mes = 2 
anio = 2024
ventas_mes = generarDatosMes(mes, anio)

# Ejemplo de uso
print("\nOpciones de productos:")
for i in range(len(PRODUCTOS)):
    print(f"{i + 1}. {PRODUCTOS[i]}")

opcion = int(input("Seleccione un producto (1-5): "))
if opcion >= 1 and opcion <=5:
    producto_seleccionado = PRODUCTOS[opcion - 1]
    mostrarTotalPorProductoYModelo(ventas_mes, producto_seleccionado)
else:
    print("Opción no válida.")


print("\n Ventas individuales")
for venta in ventas_mes: #Esto tiene que desaparecer, porque sino desapareceemos nosotros
    print(venta)


resumen_clientes = calcularFacturacionPorCliente(ventas_mes)
print()
print("Lista con clientes")
for cliente in resumen_clientes:
    print(cliente)

mostrarResumen(resumen_clientes)

print("\nDetalle Del dia")
print(mostrarDetalleDelDia(ventas_mes, 4))

mostrarDetallePorDia(ventas_mes)
print("")


print(CalcularMesFacturado(ventas_mes))
print(ClientesUnicos(ventas_mes))
"""
