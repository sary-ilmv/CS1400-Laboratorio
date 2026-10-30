
"""
# Tarea 2: El Registro de los Ancestros (Diccionarios y Conjuntos)

# Tarea 2: Registro de visitas y ofrendas asignadas

# Diccionario con el ancestro (llave) y su platillo favorito (valor)
altares_familiares = {
    "Abuela Coco": "Tamales de dulce",
    "Tío Héctor": "Mole poblano",
    "Bizabuelo Julio": "Atole de chocolate"
}

# Lista con flores traídas por los visitantes (contiene duplicados)
flores_recibidas = ["Cempasúchil", "Nube", "Cempasúchil", "Terciopelo",
 "Nube", "Cempasuchil"]

# 4. Iteración en Diccionarios: Escribe un bucle for utilizando el método .items()
# para imprimir una frase por cada ancestro.
# (Ejemplo de salida esperada: "Para Abuela Coco preparamos: Tamales de dulce").

for ancestro, platillo in altares_familiares.items():
    print(f"Para {ancestro} preparamos: {platillo}")

# 5. Usa los métodos .keys() y .values() por separado para mostrar en pantalla
# únicamente los nombres de los ancestros y luego únicamente los platillos.

print("\nNombres de los ancestros:")
for ancestro in altares_familiares.keys():
    print(ancestro)

print("\nPlatillos favoritos:")
for platillo in altares_familiares.values():
    print(platillo)

# 6. Uso de Sets (Conjuntos): Para evitar contar flores repetidas en el inventario,
# convierte la lista flores_recibidas en un set usando la función set().

flores_unicas = set(flores_recibidas)

print("\nFlores sin repetir:")
print(flores_unicas)

# 7. Reflexión: ¿Cuántos elementos tenía la lista original de flores y cuántos quedaron
# en el conjunto? ¿Por qué los conjuntos (sets) son ideales para la limpieza de datos?

# La lista original tenía 6 elementos y el conjunto quedó con 3.
# Los conjuntos son ideales para limpiar datos porque eliminan automáticamente
# los elementos repetidos.
"""
