# Lista de productos
productos = [
    {'nombre': 'Arroz 15kg', 'categoria': 'Abarrotes', 'precio': 100},
    {'nombre': 'Gasesosa Pepsi 3L', 'categoria': 'Bebidas', 'precio': 12},
    {'nombre': 'Ron Cartavio', 'categoria': 'Bebidas', 'precio': 80},
]

def buscar_productos(criterio, valor):
    """
    Busca productos que coincidan con un criterio dado.
    """
    resultados = []
    for producto in productos:
        if criterio in producto and str(producto[criterio]).lower() == str(valor).lower():
            resultados.append(producto)
    return resultados

def mostrar_productos(productos):
    """
    Muestra una lista de productos.
    """
    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Categoría: {producto['categoria']}, Precio: ${producto['precio']}")

def buscar_y_mostrar():
    """
    Solicita al usuario un criterio y valor de búsqueda, y muestra los productos que coincidan.
    """
    criterio = input("Ingrese el criterio de búsqueda (nombre/categoria/precio): ").strip().lower()
    valor = input("Ingrese el valor del criterio de búsqueda: ").strip()
    
    resultados = buscar_productos(criterio, valor)
    
    if resultados:
        print(f"Productos encontrados ({len(resultados)}):")
        mostrar_productos(resultados)
    else:
        print("No se encontraron productos que coincidan con la búsqueda.")

# Llamar a la función para buscar y mostrar productos
buscar_y_mostrar()
