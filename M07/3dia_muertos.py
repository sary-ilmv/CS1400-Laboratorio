# Tarea 3: Organización de calaveritas y conteo de caracteres

calaveritas = ["Alebrije", "Catrina", "Cempasúchil", "Pan de muerto", "Papel picado"]

# Filtrar palabras que tengan más de 7 letras (Método tradicional)
largas_tradicional = []
for elemento in calaveritas:
    if len(elemento) > 7:
        largas_tradicional.append(elemento)

print("Palabras largas (Tradicional):", largas_tradicional)

# 8. Comprensión de Listas (List Comprehension): Re-escribe el bloque de código anterior
# en una sola línea utilizando comprensión de listas para crear largas_comprehension.

largas_comprehension = [elemento for elemento in calaveritas if len(elemento) > 7]

print("Palabras largas (Comprensión):", largas_comprehension)

# 9. Utiliza una comprensión de listas para convertir todos los elementos de la lista
# calaveritas a mayúsculas usando .upper().

calaveritas_mayusculas = [elemento.upper() for elemento in calaveritas]

print("Calaveritas en mayúsculas:", calaveritas_mayusculas)

# 10. Comprensión de Diccionarios (Dictionary Comprehension): Crea un diccionario a
# partir de la lista calaveritas donde la llave sea el nombre del elemento y el valor
# sea la cantidad de letras que tiene esa palabra (usando la función len()).

conteo_caracteres = {elemento: len(elemento) for elemento in calaveritas}

print("Cantidad de caracteres:", conteo_caracteres)

# 11. Pregunta de análisis: ¿Qué ventaja ofrece escribir la solución con comprensiones
# en lugar de usar un bucle for tradicional con un .append()?

# Las comprensiones permiten escribir el código en menos líneas,
# hacen que sea más fácil de leer y ayudan a crear listas y diccionarios rápidamente.

