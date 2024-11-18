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

"""   
    Genera un identificador único dentro de un rango especificado.
    
    Precondición:
    - El parámetro PARAMETROS_ID debe ser una lista  que contenga exactamente dos valores numéricos:
      el límite inferior y el límite superior del rango, ambos incluidos.

    Postcondición:
    - Devuelve un número entero aleatorio dentro del rango especificado, cumpliendo con los límites definidos por PARAMETROS_ID.

"""
def generarID(PARAMETROS_ID):
    id_cliente = random.randint(PARAMETROS_ID[0], PARAMETROS_ID[1])
    return id_cliente

"""
    Selecciona aleatoriamente un modelo de una lista proporcionada.

    Precondición:
    - El parámetro MODELOS debe ser una lista que contenga al menos un elemento.

    Postcondición:
    - Devuelve un elemento seleccionado aleatoriamente de la lista MODELOS.
"""
def generarModelo(MODELOS):
    modelo = random.choice(MODELOS)
    return modelo

"""
    Selecciona aleatoriamente un producto de una lista proporcionada.

    Precondición:
    - El parámetro PRODUCTOS debe ser una lista que contenga al menos un elemento.

    Postcondición:
    - Devuelve un elemento seleccionado aleatoriamente de la lista PRODUCTOS.
"""
def generarProducto(PRODUCTOS):
    producto = random.choice(PRODUCTOS)
    return producto

"""
    Calcula el precio final de un producto específico basándose en su tipo y modelo.

    Precondición:
    - El parámetro `producto` debe ser una cadena válida que represente uno de los tipos aceptados: 
      "LAMPARA DE TECHO", "LAMPARA DE PARED", "LAMPARA DE MESA", "LAMPARA DE PIE" o "LUMINARIAS".
    - El parámetro `modelo` debe ser un número entero que represente el índice del modelo del producto (comenzando en 1).
    - Las listas `PRECIO_LAMP_TECHO`, `PRECIO_LAMP_PARED`, `PRECIO_LAMP_MESA`, `PRECIO_LAMP_PIE`, y `PRECIO_LUMINARIA` 
      deben estar definidas previamente y contener los precios correspondientes a cada modelo.

    Postcondición:
    - Devuelve el precio del modelo correspondiente al producto indicado.
    - Si el producto no coincide con ninguna opción válida, devuelve 0.
"""
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
            
"""
    Determina la cantidad de días de un mes específico en un año dado, considerando si el año es bisiesto.

    Precondición:
    - El parámetro `mes` debe ser un número entero entre 1 y 12 que represente un mes válido.
    - El parámetro `anio` debe ser un número entero que represente un año válido.

    Postcondición:
    - Devuelve un número entero que indica la cantidad de días del mes especificado.
    - Si el año es bisiesto, devuelve 29 días para febrero.
"""            
def obtenerDias(mes, anio):
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Comprobamos si es un año bisieso
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        dias_por_mes[1] = 29  # Si es bisiesto, febrero tiene 29 días

    return dias_por_mes[mes - 1]

"""
    Genera una lista con todos los días de un mes específico en un año dado.

    Precondición:
    - El parámetro `mes` debe ser un entero entre 1 y 12, donde 1 representa enero y 12 representa diciembre.
    - El parámetro `anio` debe ser un entero válido que represente un año (puede ser positivo o negativo).

    Postcondición:
    - Devuelve una lista donde cada elemento representa un día del mes indicado, del 1 al número total de días del mes.
"""
def generarMes(mes, anio):

    diasDelMes = []

    for i in range(obtenerDias(mes, anio)):
        
        dia = (i + 1)
        diasDelMes.append(dia)
        
    return diasDelMes

"""
    Genera aleatoriamente la cantidad de ventas de un día dentro de un rango especificado.

    Precondición:
    - El parámetro `VENTASPORDIA` debe ser una lista que contenga exactamente dos valores numéricos:
      el límite inferior y el límite superior del rango, ambos incluidos.
    - Los valores de `VENTASPORDIA[0]` y `VENTASPORDIA[1]` deben ser números enteros positivos o cero,
      con `VENTASPORDIA[0]` <= `VENTASPORDIA[1]`.

    Postcondición:
    - Devuelve un número entero aleatorio que representa la cantidad de ventas en un día, 
      dentro del rango especificado por `VENTASPORDIA`.
    """
def generarVentas(VENTASPORDIA):
    cantVentas = random.randint(VENTASPORDIA[0],VENTASPORDIA[1])
    return cantVentas

"""
    Genera una lista de datos que representa las ventas realizadas durante un mes específico en un año dado. 
    Cada dato incluye la fecha, un ID de cliente, un producto y su modelo.

    Precondición:
    - El parámetro `mes` debe ser un entero entre 1 y 12, donde 1 representa enero y 12 representa diciembre.
    - El parámetro `anio` debe ser un entero válido que represente un año (puede ser positivo o negativo).

    Postcondición:
    - Devuelve una lista donde cada elemento representa una venta con el formato:
      `[fecha, clienteId, producto, modelo]`.
    - La lista incluye todas las ventas generadas para cada día del mes.
"""
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

"""
    Calcula el total facturado, la cantidad de ventas y el costo total de los productos vendidos en un mes.

    Precondición:
    - El parámetro `ventas_mes` debe ser una lista donde cada elemento representa una venta 
      con el formato `[fecha, clienteId, producto, modelo]`.

    Postcondición:
    - Devuelve tres valores:
        1. `totalFacturado`: La suma de los precios de todas las ventas del mes.
        2. `ventasTotales`: La cantidad total de ventas realizadas en el mes.
        3. `totalCosto`: La suma de los costos de todos los productos vendidos.
"""
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

"""
    Calcula la cantidad de clientes únicos que realizaron compras durante un período dado.

    Precondición:
    - El parámetro `ventas_mes` debe ser una lista donde cada elemento representa una venta 
      con el formato `[fecha, clienteId, producto, modelo]`.
    - Cada `clienteId` debe ser un identificador único para cada cliente.

    Postcondición:
    - Devuelve un número entero que representa la cantidad de clientes únicos identificados en `ventas_mes`.
"""
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

"""
    Muestra un resumen detallado de los totales del mes, incluyendo el total facturado, 
    el número de ventas, clientes únicos y el costo total de adquisición de productos.

    Precondición:
    - El parámetro `ventas_mes` debe ser una lista donde cada elemento representa una venta 
      con el formato `[fecha, clienteId, producto, modelo]`.
    - El parámetro `mes` debe ser un entero entre 1 y 12, donde 1 representa enero y 12 representa diciembre.
    - El parámetro `anio` debe ser un entero válido que represente el año.

    Postcondición:
    - Muestra por consola los siguientes detalles del mes especificado:
        1. El mes y año.
        2. El total facturado (suma de los precios de todas las ventas).
        3. El total de ventas realizadas.
        4. El total de clientes únicos.
        5. El costo total de adquisición de los productos vendidos.
"""
def mostrarTotalMes(ventas_mes, mes, anio):
    totalFacturado,ventasTotales,totalCosto = CalcularMesFacturado(ventas_mes)
    clientesUnicos = ClientesUnicos(ventas_mes)
    print("Opcion 1: Totales Mes\n")
    print(f"Mes: {mes} {anio}\n")
    print(f"Total Facturado: ${totalFacturado}")
    print(f"Total ventas realizadas: {ventasTotales}")
    print(f"Total cliente unicos: {clientesUnicos}")
    print(f"Total Costo adquisición productos vendidos: ${totalCosto}")
    
"""
    Calcula el costo de adquisición de un producto vendido como la mitad de su precio de venta.

    Precondición:
    - El parámetro `vendido` debe ser una lista que represente una venta con el formato:
      `[fecha, clienteId, producto, modelo]`.

    Postcondición:
    - Devuelve un número entero que representa el costo de adquisición del producto vendido,
      calculado como la mitad del precio de venta.
"""
def calcularCostoProducto(vendido):
    precio = calcularPrecios(vendido[2],vendido[3])
    return precio // 2

"""
    Genera un resumen de facturación por cliente a partir de las ventas realizadas en un período determinado.

    Precondición:
    - El parámetro `ventas_mes` debe ser una lista donde cada elemento representa una venta 
      con el formato `[fecha, clienteId, producto, modelo]`.

    Postcondición:
    - Devuelve una lista `resumen_clientes` en la que cada elemento tiene el formato:
      `[clienteId, cantidad_ventas, total_facturado]`.
    - Cada cliente se registra solo una vez en el resumen.
"""
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

"""
    Muestra un detalle ordenado de la facturación por cliente, con los clientes organizados 
    de mayor a menor según el total facturado.

    Precondición:
    - El parámetro `ventas_mes` debe ser una lista donde cada elemento representa una venta
      con el formato `[fecha, clienteId, producto, modelo]`.
    - `mes` y `anio` deben ser valores válidos que representen un mes y un año.

    Postcondición:
    - Muestra por pantalla un listado ordenado de clientes, incluyendo:
      - ID del cliente
      - Total de artículos comprados
      - Total facturado
    - Los clientes se presentan de mayor a menor según el total facturado.
"""
def mostrarCalcularFacturacionPorCliente(ventas_mes, mes, anio):
    resumen_clientes = calcularFacturacionPorCliente(ventas_mes)
    
    for i in range(len(resumen_clientes)):
        for j in range(i + 1, len(resumen_clientes)):
            if resumen_clientes[i][2] < resumen_clientes[j][2]: 
                aux = resumen_clientes[i]
                resumen_clientes[i] = resumen_clientes[j]
                resumen_clientes[j] = aux
                 
    
    print("Opcion 3: Detalle por Clientes")
    print(f"Mes: {mes} {anio}")
    print(f"{'ID cliente':<10} {'Total artículos':<15} {'Total facturado':<15}")
    for i in range(len(resumen_clientes)):
        cliente_id = resumen_clientes[i][0]
        total_articulos = resumen_clientes[i][1]
        total_facturado = resumen_clientes[i][2]
        print(f"{cliente_id:<10} {total_articulos:<15} ${total_facturado:<15}")
        
"""
    Genera un resumen de las ventas realizadas en un día específico. El resumen incluye el ID del cliente, 
    el producto comprado, el modelo y el precio calculado para cada venta del día. Además, ordena el 
    resultado por el ID del cliente de menor a mayor.

    Precondición:
    - El parámetro `ventas_mes` debe ser una lista de ventas, donde cada venta tiene el formato:
      `[fecha, clienteId, producto, modelo]`.

    Postcondición:
    - Retorna una lista con el detalle de las ventas del día, donde cada venta es una lista con los siguientes 
      elementos:
      `[clienteId, producto, modelo, precio]`.
    - La lista está ordenada por `clienteId` de menor a mayor.
    """
def detalleDelDia(ventas_mes, dia):
    resultado = []
    for i in range(len(ventas_mes)):
        if ventas_mes[i][0] == dia:
            resultado.append([ventas_mes[i][1], ventas_mes[i][2], ventas_mes[i][3], calcularPrecios(ventas_mes[i][2], ventas_mes[i][3])])
   
    for i in range(len(resultado) - 1):
        for j in range(len(resultado) - 1 - i):
            if resultado[j][0] > resultado[j + 1][0]:
                aux = resultado[j]
                resultado[j] = resultado[j + 1]
                resultado[j + 1] = aux    
    return resultado

"""
    Muestra el detalle de las ventas realizadas en un día específico de un mes y año dados. 
    El detalle incluye el ID del cliente, el tipo de producto, el modelo y el total facturado por cada venta. 
    La función solicita al usuario un día, valida que sea un día válido para el mes y año dados, 
    y luego muestra la información correspondiente.

    Precondición:
    - El parámetro `ventas_mes` debe ser una lista de ventas, donde cada venta tiene el formato:
      `[fecha, clienteId, producto, modelo]`.
    - El parámetro `mes` debe ser un número entre 1 y 12 (inclusive).
    - El parámetro `anio` debe ser un año válido.

    Postcondición:
    - Si el día ingresado es válido, la función muestra el detalle de las ventas de ese día con la siguiente información:
      `ID cliente`, `Tipo de producto`, `Modelo`, `Total facturado`.
    - Si el día ingresado no es válido, muestra un mensaje de error indicando que el día debe ser válido.
"""
def mostrarDetalleDelDia(ventas_mes, mes, anio):
    dia = int(input("Ingrese un día: "))
    dias_del_mes = obtenerDias(mes, anio)
    if dia <= dias_del_mes:
        detalle = detalleDelDia(ventas_mes, dia)
        print("Opcion 5: Detalle del día")
        print(f"Mes: {mes} {anio}")
        print(f"{'ID cliente':<10} {'Tipo de producto':<15} {'Modelo':<15} {'Total facturado':<15}")
        for i in range(len(detalle)):
            cliente_id = detalle[i][0]
            tipo_producto = detalle[i][1]
            tpo_modelo = detalle[i][2]
            total_facturado = detalle[i][3]
            print(f"{cliente_id:<10} {tipo_producto:<15} {tpo_modelo:<15} ${total_facturado:<15}")
        
    else:
        print("Ingrese un día valido")
    
"""
    Breve descripción:
    Esta función calcula el total de ventas por día, acumulando las ventas realizadas en un mismo día y
    almacenando el número de ventas y el total facturado para cada día. La información se almacena en
    una lista que contiene el día, el número total de ventas y el total facturado en ese día.

    Precondición:
    - El parámetro `ventas_mes` debe ser una lista de ventas, donde cada venta tiene el formato:
      `[fecha, clienteId, producto, modelo]`.
    - Las ventas en la lista deben estar ordenadas cronológicamente o al menos agrupadas por fecha consecutiva,
      ya que la función compara ventas consecutivas para identificar las realizadas el mismo día.

    Postcondición:
    - La función devuelve una lista de detalles de ventas por día, donde cada elemento tiene el formato:
      `[fecha, total ventas en el día, total facturado en el día]`.
    - La función también acumula el total de ventas y el total facturado para cada día.

    Nota:
    - La función asume que las ventas están ordenadas cronológicamente.
"""
def detallePorDia(ventas_mes): 
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

"""
    Esta función muestra un resumen detallado de las ventas por día en un mes determinado, 
    incluyendo el total de ventas realizadas y el total facturado por cada día. 
    Utiliza la función `detallePorDia` para obtener la información agregada de ventas diarias.

    Precondición:
    - El parámetro `ventas_mes` debe ser una lista de ventas, donde cada venta tiene el formato:
      `[fecha, clienteId, producto, modelo]`.
    - El parámetro `mes` debe ser un número entero que represente el mes del año.
    - El parámetro `anio` debe ser un número entero que represente el año.

    Postcondición:
    - La función imprime en consola el resumen de ventas por día para el mes y año especificados, incluyendo:
      - Día
      - Total de ventas realizadas en ese día
      - Total facturado en ese día.
"""
def mostrarDetallePorDia(ventas_mes, mes ,anio):
    resultado_por_dia = detallePorDia(ventas_mes)
    print("Opcion 4: Detalle por día")
    print(f"Mes: {mes} {anio}")
    print(f"{'Dia':<10} {'Total ventas realizadas':<15} {'Total facturado del dia':<15}")
    for i in range(len(resultado_por_dia)):
        dia = resultado_por_dia[i][0]
        total_ventas = resultado_por_dia[i][1]
        total_facturado = resultado_por_dia[i][2]
        print(f"{dia:<10} {total_ventas:<15} ${total_facturado:<15}")
        
"""
    Esta función muestra un menú para que el usuario seleccione un producto de una lista predefinida. 
    Devuelve el producto seleccionado basado en la opción ingresada por el usuario.

    Precondición:
    - La lista `PRODUCTOS` debe estar definida y contener al menos 5 elementos, cada uno representando un tipo de producto, en el siguiente orden:
      1. Lampara de Techo
      2. Lampara de Pared
      3. Lampara de Mesa
      4. Lampara de Pie
      5. Luminarias

    Postcondición:
    - Si el usuario selecciona una opción válida (entre 1 y 5), la función devuelve el nombre del producto correspondiente.
    - Si el usuario ingresa una opción fuera de este rango, la función devuelve la cadena "Inexistente".
"""
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
        return "Inexistente"
    
"""
    Esta función calcula el total facturado, el número de ventas, las ventas por modelo, la cantidad de clientes únicos 
    y el total del costo de adquisición para un producto seleccionado durante un mes. Filtra las ventas basándose en el producto seleccionado
    y genera un resumen de las estadísticas de ventas.

    Precondición:
    - `ventas_mes` debe ser una lista de ventas donde cada venta es una lista con los siguientes elementos:
      [dia, cliente_id, producto, modelo], donde:
        - `producto` debe ser uno de los productos predefinidos (como "LAMPARA DE TECHO", etc.).
        - `modelo` debe ser un valor numérico que representa el modelo del producto.
    - `producto_seleccionado` debe ser un string que corresponde a un producto existente en las ventas (por ejemplo, "LAMPARA DE TECHO").
    
    Postcondición:
    - Si se encuentran ventas para el producto seleccionado, la función devuelve una lista con las siguientes estadísticas:
      [producto_seleccionado, total_facturado, total_ventas, ventas_por_modelo, cantidad_de_clientes_unicos, total_costo]
      donde:
        - `total_facturado` es la suma de los precios de todas las ventas del producto seleccionado.
        - `total_ventas` es el número de ventas realizadas para el producto seleccionado.
        - `ventas_por_modelo` es una lista de 4 elementos con el número de ventas por cada modelo (del 1 al 4).
        - `cantidad_de_clientes_unicos` es el número de clientes que compraron el producto seleccionado.
        - `total_costo` es la suma de los costos de adquisición de los productos vendidos.
    - Si no se encuentran ventas para el producto seleccionado, se imprime un mensaje y la función devuelve -1.
"""
def totalPorProductoYModelo(ventas_mes, producto_seleccionado):
    ventas_filtradas = []
    for i in range(len(ventas_mes)):
        if ventas_mes[i][2] == producto_seleccionado:
            ventas_filtradas.append(ventas_mes[i])

    if not ventas_filtradas:
        print(f"No se encontraron ventas para el producto seleccionado")
        return -1

    total_facturado = 0
    total_ventas = 0
    ventas_por_modelo = [0, 0, 0, 0]  
    clientes_unicos = []  
    total_costo = 0

    for i in range(len(ventas_filtradas)):
        venta = ventas_filtradas[i]
        modelo = venta[3]
        cliente_id = venta[1]
        precio = calcularPrecios(venta[2], modelo)
        costo = calcularCostoProducto(venta)

        total_facturado += precio
        total_costo += costo
        total_ventas += 1

        ventas_por_modelo[modelo - 1] += 1

        cliente_existe = False
        for j in range(len(clientes_unicos)):
            if clientes_unicos[j] == cliente_id:
                cliente_existe = True
        if not cliente_existe:
            clientes_unicos.append(cliente_id)
            
        return[producto_seleccionado, total_facturado, total_ventas, ventas_por_modelo, len(clientes_unicos), total_costo]
    
"""
    Esta función solicita al usuario seleccionar un producto, luego obtiene las estadísticas de ventas para el producto seleccionado 
    y muestra la información detallada sobre el total facturado, el número de ventas por modelo, los clientes únicos y el costo 
    de adquisición de los productos vendidos durante el mes y año especificados.

    Precondición:
    - `ventas_mes` debe ser una lista de ventas donde cada venta contiene información sobre el día, cliente, producto y modelo.
    - `mes` y `anio` deben ser valores enteros que representan el mes y el año para los cuales se mostrarán las estadísticas.
    - La función `seleccionarProducto` debe devolver un producto válido (como "LAMPARA DE TECHO", "LAMPARA DE PARED", etc.), 
      que estará disponible en las ventas de `ventas_mes`.
    - La función `totalPorProductoYModelo` debe ser capaz de calcular y devolver estadísticas completas para el producto seleccionado.

    Postcondición:
    - Si el producto seleccionado tiene ventas en el mes, se imprimen las estadísticas del producto:
      - El producto seleccionado.
      - El total facturado.
      - El total de ventas realizadas.
      - Las ventas desglosadas por modelo (modelo 1, modelo 2, modelo 3, modelo 4).
      - La cantidad de clientes únicos.
      - El total del costo de adquisición de los productos vendidos.
    - Si no hay ventas para el producto seleccionado, se indica que no se encontraron ventas y no se muestran estadísticas.
"""
def mostrarTotalPorProductoYModelo(ventas_mes, mes, anio):
    producto_seleccionado = seleccionarProducto()
    total = totalPorProductoYModelo(ventas_mes, producto_seleccionado)
    if total != -1:
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
        
"""
    Esta función imprime un menú en la consola con las diferentes opciones disponibles para el usuario, 
    permitiéndole elegir entre distintas funcionalidades relacionadas con las ventas de productos de iluminación.

    Precondición:
    - No requiere parámetros de entrada.

    Postcondición:
    - Se imprime un menú con las siguientes opciones:
      1. Opción 1: Totales Mes
      2. Opción 2: Total por tipo de Producto y modelo
      3. Opción 3: Detalle por Clientes
      4. Opción 4: Detalle por día
      5. Opción 5: Detalle del día
      6. Opción 6: SALIR
"""
def mostrarOpcionesMenu():
    print("ILUMINACION")
    print("------------------")
    print("1...............Opcion 1: Totales Mes")
    print("2...............Opcion 2: Total por tipo de Producto y modelo")
    print("3...............Opcion 3: Detalle por Clientes")
    print("4...............Opcion 4: Detalle por día")
    print("5...............Opcion 5: Detalle del día")
    print("6...............Opcion 6: SALIR")
    
"""
    Esta función implementa un menú interactivo en la consola que permite al usuario seleccionar 
    una opción para visualizar diferentes informes de ventas relacionados con un mes y un año específicos.

    Precondición:
    - `ventas_mes`: Una lista de ventas, donde cada venta contiene datos como fecha, cliente, producto, modelo, etc.
    - `mes`: El mes del año para el que se desean consultar los datos.
    - `anio`: El año para el que se desean consultar los datos.

    Postcondición:
    - Muestra un menú de opciones, y según la opción seleccionada, se ejecuta la funcionalidad correspondiente.
    - Si se elige una opción no válida, se muestra un mensaje de error.
    - Si se selecciona la opción 6, el programa terminará.
"""
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
            elif opcion == 3:
                mostrarCalcularFacturacionPorCliente(ventas_mes, mes, anio)
            elif opcion == 4:
                mostrarDetallePorDia(ventas_mes, mes, anio)
            elif opcion == 5:
                mostrarDetalleDelDia(ventas_mes, mes, anio)
            elif opcion == 6:
                bandera = False
                print("Saliendo del programa...")
            else: 
                print("Ha ocurrido un error")
        else: 
            print("Ingrese una opcion válida")
    
"""
    Esta función solicita al usuario que ingrese un mes y un año, y valida que el mes esté dentro del rango válido (1 a 12).
    
    Precondición:
    - El usuario debe ingresar valores numéricos para el mes y el año.

    Postcondición:
    - Si el mes está en el rango válido (1 a 12), la función retorna una lista con el mes y el año.
    - Si el mes no está en el rango válido, la función retorna -1.
    """
def ingresarMesyAnio():
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))
    if mes>= 1 and mes <= 12:
        return [mes, anio]
    else: 
        return -1
    
"""
    Función principal que coordina la ejecución del programa.
    
    1. Solicita al usuario el mes y el año a través de la función `ingresarMesyAnio`.
    2. Si el mes y el año son válidos (no retornan -1), genera los datos del mes con `generarDatosMes` y muestra el menú con la función `menu`.
    3. Si los datos ingresados no son válidos, muestra un mensaje de error y solicita la entrada nuevamente.
"""
def main():
    datos = ingresarMesyAnio()
    if datos != -1: 
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
