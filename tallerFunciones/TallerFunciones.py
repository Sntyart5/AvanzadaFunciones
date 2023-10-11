# Función para calcular el subtotal
def calcular_subtotal(precio, cantidad):
    if precio > 0 and cantidad > 0:
        return precio * cantidad
    else:
        return 0

# Función para calcular el descuento
def calcular_descuento(subtotal, descuento):
    return subtotal * (descuento / 100)

# Función para calcular el IVA
def calcular_iva(subtotal, descuento):
    return (subtotal - descuento) * 0.19

# Función para calcular el total a pagar
def calcular_total(subtotal, descuento):
    return subtotal - descuento + calcular_iva(subtotal, descuento)

# Contadores y acumuladores
ventas = 0
total_ventas = 0

while True:
    opcion = input("Desea ingresar datos? 1.Si 2. No: ")
    if opcion == "2":
        break

    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad vendida: "))
    descuento = float(input("Ingrese el porcentaje de descuento: "))

    subtotal = calcular_subtotal(precio, cantidad)
    valor_descuento = calcular_descuento(subtotal, descuento)
    iva = calcular_iva(subtotal, valor_descuento)
    total_pagar = calcular_total(subtotal, valor_descuento)

    print("FACTURA DE VENTA")
    print("Código del producto:", codigo)
    print("Nombre Producto:", nombre)
    print("Precio:", precio)
    print("Cantidad:", cantidad)
    print("Subtotal:", subtotal)
    print("Descuento:", descuento, "%")
    print("Valor de Descuento:", valor_descuento)
    print("Iva:", iva)
    print("Total a Pagar:", total_pagar)

    ventas += 1
    total_ventas += total_pagar

print("Número de ventas:", ventas)
print("Total de todas las ventas registradas:", total_ventas)
