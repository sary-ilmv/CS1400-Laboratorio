# gestion_tienda.py

# Este módulo contiene las funciones para gestionar el inventario de la tienda.
# Crear las 3 funciones que se describen a continuación:
# Una para agregar un producto, debe recibir inventario, nombre y precio.
# Esta debe tener un try except ValueError para manejar el error si el precio no es un número.
# Otra para buscar el precio de un producto, debe recibir inventario y nombre. Utiliza .get()
# Y una última función para listar todos los productos, debe recibir el inventario.
# Tener una opcion por si esta vacio el inventario.

# TODO #3 Agregar comentarios a cada función explicando qué hace y cómo funciona.

def agregar_producto(inventario, nombre, precio):
    """
    Revise esta funcion y le faltaba validar cuando meten un precio texto
    Lo solucione convirtiendo el precio a float con un try-except. Si pasa lo guardo 
    en el inventario y regresa True; si marca ValueError devuelvo False
    """
    try:
        # Convertimos a float para asegurar que sea un número
        precio_num = float(precio)
        inventario[nombre] = precio_num
        return True
    except ValueError:
        # Si no se puede convertir a número, devolvemos False
        return False


def buscar_precio(inventario, nombre):
    """
    Aqui le faltaba evitar que el programa se cayera si buscan un producto que no existe
    Le puse el método .get() directo al diccionario para que si no encuentra la clave devuelva None
    """
    # Usamos .get() para evitar que el programa falle si la llave no existe
    return inventario.get(nombre, None)


def listar_productos(inventario):
    """
    En esta funcion faltaba la condición por si la tienda no tiene productos todavia
    Le agregue un if not inventario para mandar el aviso de que está vacio, 
    y si si hay elementos, los recorro con un for para imprimirlos ordenados
    """
    if not inventario:
        print("\n> El inventario está vacío.")
    else:
        print("\n--- Inventario Actual ---")
        for producto, precio in inventario.items():
            print(f"• {producto}: ${precio:.2f}")